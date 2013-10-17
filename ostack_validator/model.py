import os.path
import re
import logging
from itertools import groupby

from ostack_validator.common import Mark, Issue, MarkedIssue
from ostack_validator.schema import ConfigSchemaRegistry, TypeValidatorRegistry
from ostack_validator.config_model import Configuration
import ostack_validator.schemas
from ostack_validator.config_formats import IniConfigParser
from ostack_validator.utils import memoized


class IssueReporter(object):

    def __init__(self):
        super(IssueReporter, self).__init__()
        self.issues = []

    def report_issue(self, issue):
        issue.subject = self
        self.issues.append(issue)

    @property
    def all_issues(self):
        return list(self.issues)


class Openstack(IssueReporter):

    def __init__(self):
        super(Openstack, self).__init__()
        self.hosts = []

    def add_host(self, host):
        if not host:
            return

        self.hosts.append(host)
        host.parent = self

    @property
    def all_issues(self):
        result = super(Openstack, self).all_issues

        for host in self.hosts:
            result.extend(host.all_issues)

        return result

    @property
    def components(self):
        components = []
        for host in self.hosts:
            components.extend(host.components)

        return components


class Host(IssueReporter):

    def __init__(self, name):
        super(Host, self).__init__()
        self.name = name
        self.components = []

    def __str__(self):
        return 'Host "%s"' % self.name

    def add_component(self, component):
        if not component:
            return

        self.components.append(component)
        component.parent = self

    @property
    def openstack(self):
        return self.parent

    @property
    def all_issues(self):
        result = super(Host, self).all_issues

        for component in self.components:
            result.extend(component.all_issues)

        return result


class Service(IssueReporter):

    def __init__(self):
        super(Service, self).__init__()
        self.issues = []

    def report_issue(self, issue):
        self.issues.append(issue)

    @property
    def host(self):
        return self.parent

    @property
    def openstack(self):
        return self.host.openstack

    @property
    def all_issues(self):
        result = super(Service, self).all_issues

        if hasattr(self, 'config_files') and self.config_files:
            [result.extend(config_file.all_issues)
             for config_file in self.config_files]

        return result

    def __str__(self):
        return 'Service "%s"' % self.name


class OpenstackComponent(Service):
    logger = logging.getLogger('ostack_validator.model.openstack_component')
    component = None

    @property
    @memoized
    def config(self):
        schema = ConfigSchemaRegistry.get_schema(self.component, self.version)
        if not schema:
            self.logger.debug(
                'No schema for component "%s" main config version %s. Skipping it' %
                (self.component, self.version))
            return None

        return self._parse_config_resources(self.config_files, schema)

    def _parse_config_resources(self, resources, schema=None):
        config = Configuration()

        # Apply defaults
        if schema:
            for parameter in filter(lambda p: p.default, schema.parameters):
                if parameter.section == 'DEFAULT':
                    config.set_default(parameter.name, parameter.default)
                else:
                    config.set_default(
                        '%s.%s' %
                        (parameter.section, parameter.name), parameter.default)

        for resource in reversed(resources):
            self._parse_config_file(
                Mark(resource.path),
                resource.contents,
                config,
                schema,
                issue_reporter=resource)

        return config

    def _parse_config_file(
        self,
        base_mark,
        config_contents,
        config=Configuration(),
        schema=None,
            issue_reporter=None):
        if issue_reporter:
            def report_issue(issue):
                issue_reporter.report_issue(issue)
        else:
            def report_issue(issue):
                pass

        # Parse config file
        config_parser = IniConfigParser()
        parsed_config = config_parser.parse('', base_mark, config_contents)
        for error in parsed_config.errors:
            report_issue(error)

        # Validate config parameters and store them
        section_name_text_f = lambda s: s.name.text
        sections_by_name = groupby(
            sorted(
                parsed_config.sections,
                key=section_name_text_f),
            key=section_name_text_f)

        for section_name, sections in sections_by_name:
            sections = list(sections)

            if len(sections) > 1:
                report_issue(
                    Issue(
                        Issue.INFO,
                        'Section "%s" appears multiple times' %
                        section_name))

            seen_parameters = set()

            for section in sections:
                unknown_section = False
                if schema:
                    unknown_section = not schema.has_section(section.name.text)

                if unknown_section:
                    report_issue(
                        MarkedIssue(Issue.WARNING, 'Unknown section "%s"' %
                                    (section_name), section.start_mark))
                    continue

                for parameter in section.parameters:
                    parameter_schema = None
                    if schema:
                        parameter_schema = schema.get_parameter(
                            name=parameter.name.text,
                            section=section.name.text)
                        if not (parameter_schema or unknown_section):
                            report_issue(
                                MarkedIssue(
                                    Issue.WARNING, 'Unknown parameter: section "%s" name "%s"' %
                                    (section_name, parameter.name.text), parameter.start_mark))
                            continue

                    if parameter.name.text in seen_parameters:
                        report_issue(
                            MarkedIssue(
                                Issue.WARNING, 'Parameter "%s" in section "%s" redeclared' %
                                (parameter.name.text, section_name), parameter.start_mark))
                    else:
                        seen_parameters.add(parameter.name.text)

                    parameter_fullname = parameter.name.text
                    if section_name != 'DEFAULT':
                        parameter_fullname = section_name + \
                            '.' + parameter_fullname

                    if parameter_schema:
                        type_validator = TypeValidatorRegistry.get_validator(
                            parameter_schema.type)
                        type_validation_result = type_validator.validate(
                            parameter.value.text)
                        if isinstance(type_validation_result, Issue):
                            type_validation_result.mark = parameter.value.start_mark.merge(
                                type_validation_result.mark)
                            type_validation_result.message = 'Property "%s" in section "%s": %s' % (
                                parameter.name.text, section_name, type_validation_result.message)
                            report_issue(type_validation_result)

                            config.set(
                                parameter_fullname,
                                parameter.value.text)
                        else:
                            value = type_validation_result

                            config.set(parameter_fullname, value)

                            # if value == parameter_schema.default:
                            #   report_issue(MarkedIssue(Issue.INFO, 'Explicit value equals default: section "%s" parameter "%s"' % (section_name, parameter.name.text), parameter.start_mark))
                        if parameter_schema.deprecation_message:
                            report_issue(
                                MarkedIssue(
                                    Issue.WARNING, 'Deprecated parameter: section "%s" name "%s". %s' %
                                    (section_name, parameter.name.text, parameter_schema.deprecation_message), parameter.start_mark))
                    else:
                        config.set(parameter_fullname, parameter.value.text)

        return config


class KeystoneComponent(OpenstackComponent):
    component = 'keystone'
    name = 'keystone'


class GlanceApiComponent(OpenstackComponent):
    component = 'glance'
    name = 'glance-api'


class GlanceRegistryComponent(OpenstackComponent):
    component = 'glance'
    name = 'glance-registry'


class NovaApiComponent(OpenstackComponent):
    component = 'nova'
    name = 'nova-api'

    @property
    @memoized
    def paste_config(self):
        return self._parse_config_resources([self.paste_config_file])

    @property
    def all_issues(self):
        result = super(NovaApiComponent, self).all_issues

        if hasattr(self, 'paste_config_file') and self.paste_config_file:
            result.extend(self.paste_config_file.all_issues)

        return result


class NovaComputeComponent(OpenstackComponent):
    component = 'nova'
    name = 'nova-compute'


class NovaSchedulerComponent(OpenstackComponent):
    component = 'nova'
    name = 'nova-scheduler'


class CinderApiComponent(OpenstackComponent):
    component = 'cinder'
    name = 'cinder-api'


class CinderVolumeComponent(OpenstackComponent):
    component = 'cinder'
    name = 'cinder-volume'


class CinderSchedulerComponent(OpenstackComponent):
    component = 'cinder'
    name = 'cinder-scheduler'


class MysqlComponent(Service):
    component = 'mysql'
    name = 'mysql'


class RabbitMqComponent(Service):
    name = 'rabbitmq'


class FileResource(IssueReporter):

    def __init__(self, path, contents, owner, group, permissions):
        super(FileResource, self).__init__()
        self.path = path
        self.contents = contents
        self.owner = owner
        self.group = group
        self.permissions = permissions

    def __str__(self):
        return 'File "%s"' % self.path
