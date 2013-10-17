from ostack_validator.schema import ConfigSchemaRegistry

cinder = ConfigSchemaRegistry.register_schema(project='cinder')

cinder.version('2013.1.3')

cinder.param('', type='string', default='', description="")

cinder.param('', type='string', default='', description="cinder.conf sample")

cinder.section('DEFAULT')

cinder.param(
    'fatal_exception_format_errors',
    type='boolean',
    default='false',
    description="make exception message format errors fatal")

cinder.param(
    'policy_file',
    type='string',
    default='policy.json',
    description="JSON file representing policy")

cinder.param(
    'policy_default_rule',
    type='string',
    default='default',
    description="Rule checked when requested rule is not found")

cinder.param(
    'quota_volumes',
    type='integer',
    default='10',
    description="number of volumes allowed per project")

cinder.param(
    'quota_snapshots',
    type='integer',
    default='10',
    description="number of volume snapshots allowed per project")

cinder.param(
    'quota_gigabytes',
    type='integer',
    default='1000',
    description="number of volume gigabytes")

cinder.param(
    'reservation_expire',
    type='integer',
    default='86400',
    description="number of seconds until a reservation expires")

cinder.param(
    'until_refresh',
    type='integer',
    default='0',
    description="count of reservations until usage is refreshed")

cinder.param(
    'max_age',
    type='integer',
    default='0',
    description="number of seconds between subsequent usage refreshes")

cinder.param(
    'quota_driver',
    type='string',
    default='cinder.quota.DbQuotaDriver',
    description="default driver to use for quota checks")

cinder.param(
    'use_default_quota_class',
    type='boolean',
    default='true',
    description="whether to use default quota class for default quota")

cinder.param(
    'report_interval',
    type='integer',
    default='10',
    description="seconds between nodes reporting state to datastore")

cinder.param(
    'periodic_interval',
    type='integer',
    default='60',
    description="seconds between running periodic tasks")

cinder.param(
    'periodic_fuzzy_delay',
    type='integer',
    default='60',
    description="range of seconds to randomly delay when starting the periodic task scheduler to reduce stampeding.")

cinder.param(
    'osapi_volume_listen',
    type='string',
    default='0.0.0.0',
    description="IP address for OpenStack Volume API to listen")

cinder.param(
    'osapi_volume_listen_port',
    type='integer',
    default='8776',
    description="port for os volume api to listen")

cinder.param(
    'sqlite_clean_db',
    type='string',
    default='clean.sqlite',
    description="File name of clean sqlite db")

cinder.param(
    'fake_tests',
    type='boolean',
    default='true',
    description="should we use everything for testing")

cinder.param(
    'backlog',
    type='integer',
    default='4096',
    description="Number of backlog requests to configure the socket with")

cinder.param(
    'tcp_keepidle',
    type='integer',
    default='600',
    description="Sets the value of TCP_KEEPIDLE in seconds for each server socket. Not supported on OS X.")

cinder.param(
    'ssl_ca_file',
    type='string',
    default='<None>',
    description="CA certificate file to use to verify connecting clients")

cinder.param(
    'ssl_cert_file',
    type='string',
    default='<None>',
    description="Certificate file to use when starting the server securely")

cinder.param(
    'ssl_key_file',
    type='string',
    default='<None>',
    description="Private key file to use when starting the server securely")

cinder.param(
    'osapi_max_limit',
    type='integer',
    default='1000',
    description="the maximum number of items returned in a single response from a collection resource")

cinder.param(
    'osapi_volume_base_URL',
    type='string',
    default='<None>',
    description="Base URL that will be presented to users in links to the OpenStack Volume API")

cinder.param(
    'use_forwarded_for',
    type='boolean',
    default='false',
    description="Treat X-Forwarded-For as the canonical remote address. Only enable this if you have a sanitizing proxy.")

cinder.param(
    'osapi_max_request_body_size',
    type='integer',
    default='114688',
    description="Max size for body of a request")

cinder.param(
    'backup_ceph_conf',
    type='string',
    default='/etc/ceph/ceph.conf',
    description="Ceph config file to use.")

cinder.param(
    'backup_ceph_user',
    type='string',
    default='cinder',
    description="the Ceph user to connect with")

cinder.param(
    'backup_ceph_chunk_size',
    type='integer',
    default='134217728',
    description="the chunk size in bytes that a backup will be broken into before transfer to backup store")

cinder.param(
    'backup_ceph_pool',
    type='string',
    default='backups',
    description="the Ceph pool to backup to")

cinder.param(
    'backup_ceph_stripe_unit',
    type='integer',
    default='0',
    description="RBD stripe unit to use when creating a backup image")

cinder.param(
    'backup_ceph_stripe_count',
    type='integer',
    default='0',
    description="RBD stripe count to use when creating a backup image")

cinder.param(
    'restore_discard_excess_bytes',
    type='boolean',
    default='true',
    description="If True, always discard excess bytes when restoring volumes.")

cinder.param(
    'backup_swift_url',
    type='string',
    default='http://localhost:8080/v1/AUTH_',
    description="The URL of the Swift endpoint")

cinder.param(
    'backup_swift_auth',
    type='string',
    default='per_user',
    description="Swift authentication mechanism")

cinder.param(
    'backup_swift_user',
    type='string',
    default='<None>',
    description="Swift user name")

cinder.param(
    'backup_swift_key',
    type='string',
    default='<None>',
    description="Swift key for authentication")

cinder.param(
    'backup_swift_container',
    type='string',
    default='volumebackups',
    description="The default Swift container to use")

cinder.param(
    'backup_swift_object_size',
    type='integer',
    default='52428800',
    description="The size in bytes of Swift backup objects")

cinder.param(
    'backup_swift_retry_attempts',
    type='integer',
    default='3',
    description="The number of retries to make for Swift operations")

cinder.param(
    'backup_swift_retry_backoff',
    type='integer',
    default='2',
    description="The backoff time in seconds between Swift retries")

cinder.param(
    'backup_compression_algorithm',
    type='string',
    default='zlib',
    description="Compression algorithm")

cinder.param(
    'backup_tsm_volume_prefix',
    type='string',
    default='backup',
    description="Volume prefix for the backup id when backing up to TSM")

cinder.param(
    'backup_tsm_password',
    type='string',
    default='password',
    description="TSM password for the running username")

cinder.param(
    'backup_tsm_compression',
    type='boolean',
    default='true',
    description="Enable or Disable compression for backups")

cinder.param(
    'backup_driver',
    type='string',
    default='cinder.backup.drivers.swift',
    description="Driver to use for backups.")

cinder.param(
    'num_volume_device_scan_tries',
    type='integer',
    default='3',
    description="The maximum number of times to rescan targetsto find volume")

cinder.param(
    'iscsi_helper',
    type='string',
    default='tgtadm',
    description="iscsi target user-land tool to use")

cinder.param(
    'volumes_dir',
    type='string',
    default='$state_path/volumes',
    description="Volume configuration file storage directory")

cinder.param(
    'iet_conf',
    type='string',
    default='/etc/iet/ietd.conf',
    description="IET configuration file")

cinder.param(
    'lio_initiator_iqns',
    type='string',
    default='',
    description="Comma-separatd list of initiator IQNs allowed to connect to the iSCSI target.")

cinder.param(
    'iscsi_iotype',
    type='string',
    default='fileio',
    description="Sets the behavior of the iSCSI target to either perform blockio or fileio optionally, auto can be set and Cinder will autodetect type of backing device")

cinder.param(
    'iser_helper',
    type='string',
    default='tgtadm',
    description="iser target user-land tool to use")

cinder.param(
    'volumes_dir',
    type='string',
    default='$state_path/volumes',
    description="Volume configuration file storage directory")

cinder.param(
    'nfs_mount_point_base',
    type='string',
    default='$state_path/mnt',
    description="Base dir containing mount points for nfs shares")

cinder.param(
    'nfs_mount_options',
    type='string',
    default='<None>',
    description="Mount options passed to the nfs client. See section of the nfs man page for details")

cinder.param(
    'glusterfs_mount_point_base',
    type='string',
    default='$state_path/mnt',
    description="Base dir containing mount points for gluster shares")

cinder.param(
    'connection_type',
    type='string',
    default='<None>',
    description="Virtualization api connection type : libvirt, xenapi, or fake")

cinder.param(
    'api_paste_config',
    type='string',
    default='api-paste.ini',
    description="File name for the paste.deploy config for cinder-api")

cinder.param(
    'pybasedir',
    type='string',
    default='/usr/lib/python/site-packages',
    description="Directory where the cinder python module is installed")

cinder.param(
    'bindir',
    type='string',
    default='$pybasedir/bin',
    description="Directory where cinder binaries are installed")

cinder.param(
    'state_path',
    type='string',
    default='$pybasedir',
    description="Top-level directory for maintaining cinder's state")

cinder.param(
    'my_ip',
    type='string',
    default='10.0.0.1',
    description="ip address of this host")

cinder.param(
    'glance_host',
    type='string',
    default='$my_ip',
    description="default glance hostname or ip")

cinder.param(
    'glance_port',
    type='integer',
    default='9292',
    description="default glance port")

cinder.param(
    'glance_api_servers',
    type='list',
    default='$glance_host:$glance_port',
    description="A list of the glance api servers available to cinder")

cinder.param(
    'glance_api_version',
    type='integer',
    default='1',
    description="Version of the glance api to use")

cinder.param(
    'glance_num_retries',
    type='integer',
    default='0',
    description="Number retries when downloading an image from glance")

cinder.param(
    'glance_api_insecure',
    type='boolean',
    default='false',
    description="Allow to perform insecure SSL")

cinder.param(
    'glance_api_ssl_compression',
    type='boolean',
    default='false',
    description="Whether to attempt to negotiate SSL layer compression when using SSL")

cinder.param(
    'glance_request_timeout',
    type='integer',
    default='<None>',
    description="http/https timeout value for glance operations. If no value")

cinder.param(
    'scheduler_topic',
    type='string',
    default='cinder-scheduler',
    description="the topic scheduler nodes listen on")

cinder.param(
    'volume_topic',
    type='string',
    default='cinder-volume',
    description="the topic volume nodes listen on")

cinder.param(
    'backup_topic',
    type='string',
    default='cinder-backup',
    description="the topic volume backup nodes listen on")

cinder.param(
    'enable_v1_api',
    type='boolean',
    default='true',
    description="Deploy v1 of the Cinder API. ")

cinder.param(
    'enable_v2_api',
    type='boolean',
    default='true',
    description="Deploy v2 of the Cinder API. ")

cinder.param(
    'api_rate_limit',
    type='boolean',
    default='true',
    description="whether to rate limit the api")

cinder.param(
    'osapi_volume_ext_list',
    type='list',
    default='',
    description="Specify list of extensions to load when using osapi_volume_extension option with cinder.api.contrib.select_extensions")

cinder.param(
    'osapi_volume_extension',
    type='multi',
    default='cinder.api.contrib.standard_extensions',
    description="osapi volume extension to load")

cinder.param(
    'volume_manager',
    type='string',
    default='cinder.volume.manager.VolumeManager',
    description="full class name for the Manager for volume")

cinder.param(
    'backup_manager',
    type='string',
    default='cinder.backup.manager.BackupManager',
    description="full class name for the Manager for volume backup")

cinder.param(
    'scheduler_manager',
    type='string',
    default='cinder.scheduler.manager.SchedulerManager',
    description="full class name for the Manager for scheduler")

cinder.param(
    'host',
    type='string',
    default='cinder',
    description="Name of this node.  This can be an opaque identifier.  It is not necessarily a hostname, FQDN, or IP address.")

cinder.param(
    'storage_availability_zone',
    type='string',
    default='nova',
    description="availability zone of this node")

cinder.param(
    'default_availability_zone',
    type='string',
    default='<None>',
    description="default availability zone to use when creating a new volume. If this is not set then we use the value from the storage_availability_zone option as the default availability_zone for new volumes.")

cinder.param(
    'memcached_servers',
    type='list',
    default='<None>',
    description="Memcached servers or None for in process cache.")

cinder.param(
    'default_volume_type',
    type='string',
    default='<None>',
    description="default volume type to use")

cinder.param(
    'volume_usage_audit_period',
    type='string',
    default='month',
    description="time period to generate volume usages for.  Time period must be hour, day, month or year")

cinder.param(
    'root_helper',
    type='string',
    default='sudo',
    description="Deprecated: command to use for running commands as root")

cinder.param(
    'rootwrap_config',
    type='string',
    default='/etc/cinder/rootwrap.conf',
    description="Path to the rootwrap configuration file to use for running commands as root")

cinder.param(
    'monkey_patch',
    type='boolean',
    default='false',
    description="Enable monkey patching")

cinder.param(
    'monkey_patch_modules',
    type='list',
    default='',
    description="List of modules/decorators to monkey patch")

cinder.param(
    'service_down_time',
    type='integer',
    default='60',
    description="maximum time since last check-in for up service")

cinder.param(
    'volume_api_class',
    type='string',
    default='cinder.volume.api.API',
    description="The full class name of the volume API class to use")

cinder.param(
    'backup_api_class',
    type='string',
    default='cinder.backup.api.API',
    description="The full class name of the volume backup API class")

cinder.param(
    'auth_strategy',
    type='string',
    default='noauth',
    description="The strategy to use for auth. Supports noauth, keystone, and deprecated.")

cinder.param(
    'enabled_backends',
    type='list',
    default='<None>',
    description="A list of backend names to use. These backend names should be backed by a unique [CONFIG] group with its options")

cinder.param(
    'no_snapshot_gb_quota',
    type='boolean',
    default='false',
    description="Whether snapshots count against GigaByte quota")

cinder.param(
    'transfer_api_class',
    type='string',
    default='cinder.transfer.api.API',
    description="The full class name of the volume transfer API class")

cinder.param(
    'compute_api_class',
    type='string',
    default='cinder.compute.nova.API',
    description="The full class name of the compute API class to use")

cinder.param(
    'nova_catalog_info',
    type='string',
    default='compute:nova:publicURL',
    description="Info to match when looking for nova in the service catalog. Format is : separated values of the form: <service_type>:<service_name>:<endpoint_type>")

cinder.param(
    'nova_catalog_admin_info',
    type='string',
    default='compute:nova:adminURL',
    description="Same as nova_catalog_info, but for admin endpoint.")

cinder.param(
    'nova_endpoint_template',
    type='string',
    default='<None>',
    description="Override service catalog lookup with template for nova endpoint e.g. http://localhost:8774/v2/%(tenant_id)s")

cinder.param(
    'nova_endpoint_admin_template',
    type='string',
    default='<None>',
    description="Same as nova_endpoint_template, but for admin endpoint.")

cinder.param(
    'os_region_name',
    type='string',
    default='<None>',
    description="region name of this node")

cinder.param(
    'nova_ca_certificates_file',
    type='string',
    default='<None>',
    description="Location of ca certicates file to use for nova client requests.")

cinder.param(
    'nova_api_insecure',
    type='boolean',
    default='false',
    description="Allow to perform insecure SSL requests to nova")

cinder.param(
    'db_backend',
    type='string',
    default='sqlalchemy',
    description="The backend to use for db")

cinder.param(
    'enable_new_services',
    type='boolean',
    default='true',
    description="Services to be added to the available pool on create")

cinder.param(
    'volume_name_template',
    type='string',
    default='volume-%s',
    description="Template string to be used to generate volume names")

cinder.param(
    'snapshot_name_template',
    type='string',
    default='snapshot-%s',
    description="Template string to be used to generate snapshot names")

cinder.param(
    'backup_name_template',
    type='string',
    default='backup-%s',
    description="Template string to be used to generate backup names")

cinder.param(
    'db_driver',
    type='string',
    default='cinder.db',
    description="driver to use for database access")

cinder.param(
    'allowed_direct_url_schemes',
    type='list',
    default='',
    description="A list of url schemes that can be downloaded directly via the direct_url.  Currently supported schemes: [file].")

cinder.param(
    'image_conversion_dir',
    type='string',
    default='$state_path/conversion',
    description="Directory used for temporary storage during image conversion")

cinder.param(
    'keymgr_api_class',
    type='string',
    default='cinder.keymgr.not_implemented_key_mgr.NotImplementedKeyManager',
    description="The full class name of the key manager API class")

cinder.param(
    'backend',
    type='string',
    default='sqlalchemy',
    description="The backend to use for db")

cinder.param(
    'use_tpool',
    type='boolean',
    default='false',
    description="Enable the experimental use of thread pooling for all DB API calls")

cinder.param(
    'connection',
    type='string',
    default='sqlite:////cinder/openstack/common/db/$sqlite_db',
    description="The SQLAlchemy connection string used to connect to the database")

cinder.param(
    'sql_connection',
    type='string',
    default='sqlite:////nova/openstack/common/db/$sqlite_db',
    description="The SQLAlchemy connection string used to connect to the database",
    deprecation_message='Deprecated in favor of "[DEFAULT]connection" parameter')

cinder.param(
    'idle_timeout',
    type='integer',
    default='3600',
    description="timeout before idle sql connections are reaped")

cinder.param(
    'min_pool_size',
    type='integer',
    default='1',
    description="Minimum number of SQL connections to keep open in a pool")

cinder.param(
    'max_pool_size',
    type='integer',
    default='5',
    description="Maximum number of SQL connections to keep open in a pool")

cinder.param(
    'max_retries',
    type='integer',
    default='10',
    description="maximum db connection retries during startup.")

cinder.param(
    'retry_interval',
    type='integer',
    default='10',
    description="interval between retries of opening a sql connection")

cinder.param(
    'max_overflow',
    type='integer',
    default='<None>',
    description="If set, use this value for max_overflow with sqlalchemy")

cinder.param(
    'connection_debug',
    type='integer',
    default='0',
    description="Verbosity of SQL debugging information. 0=None, 100=Everything")

cinder.param(
    'connection_trace',
    type='boolean',
    default='false',
    description="Add python stack traces to SQL as comment strings")

cinder.param(
    'sqlite_db',
    type='string',
    default='cinder.sqlite',
    description="the filename to use with sqlite")

cinder.param(
    'sqlite_synchronous',
    type='boolean',
    default='true',
    description="If true, use synchronous mode for sqlite")

cinder.param(
    'backdoor_port',
    type='integer',
    default='<None>',
    description="port for eventlet backdoor to listen")

cinder.param(
    'disable_process_locking',
    type='boolean',
    default='false',
    description="Whether to disable inter-process locks")

cinder.param(
    'lock_path',
    type='string',
    default='<None>',
    description="Directory to use for lock files. Default to a temp directory")

cinder.param(
    'debug',
    type='boolean',
    default='false',
    description="Print debugging output")

cinder.param(
    'verbose',
    type='boolean',
    default='false',
    description="Print more verbose output")

cinder.param(
    'use_stderr',
    type='boolean',
    default='true',
    description="Log output to standard error")

cinder.param(
    'logging_context_format_string',
    type='string',
    default='%(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [%(request_id)s %(user)s %(tenant)s] %(instance)s%(message)s',
    description="format string to use for log messages with context")

cinder.param(
    'logging_default_format_string',
    type='string',
    default='%(asctime)s.%(msecs)03d %(process)d %(levelname)s %(name)s [-] %(instance)s%(message)s',
    description="format string to use for log messages without context")

cinder.param(
    'logging_debug_format_suffix',
    type='string',
    default='%(funcName)s %(pathname)s:%(lineno)d',
    description="data to append to log format when level is DEBUG")

cinder.param(
    'logging_exception_prefix',
    type='string',
    default='%(asctime)s.%(msecs)03d %(process)d TRACE %(name)s %(instance)s',
    description="prefix each line of exception output with this format")

cinder.param(
    'default_log_levels',
    type='list',
    default='amqplibWARN,sqlalchemyWARN,botoWARN,sudsINFO,keystoneINFO,eventlet.wsgi.serverWARN',
    description="list of logger=LEVEL pairs")

cinder.param(
    'publish_errors',
    type='boolean',
    default='false',
    description="publish error events")

cinder.param(
    'fatal_deprecations',
    type='boolean',
    default='false',
    description="make deprecations fatal")

cinder.param(
    'instance_format',
    type='string',
    default='"[instance: %(uuid)s] "',
    description="If an instance is passed with the log message, format it like this")

cinder.param(
    'instance_uuid_format',
    type='string',
    default='"[instance: %(uuid)s] "',
    description="If an instance UUID is passed with the log message, format it like this")

cinder.param(
    'log_config',
    type='string',
    default='<None>',
    description="If this option is specified, the logging configuration file specified is used and overrides any other logging options specified. Please see the Python logging module documentation for details on logging configuration files.")

cinder.param(
    'log_format',
    type='string',
    default='<None>',
    description="A logging.Formatter log message format string which may use any of the available logging.LogRecord attributes. This option is deprecated.  Please use logging_context_format_string and logging_default_format_string instead.")

cinder.param(
    'log_date_format',
    type='string',
    default='%Y-%m-%d %H:%M:%S',
    description="Format string for %%(asctime)s in log records. Default: %(default)s")

cinder.param(
    'log_file',
    type='string',
    default='<None>',
    description="(Optional) Name of log file to output to. If no default is set, logging will go to stdout.")

cinder.param(
    'log_dir',
    type='string',
    default='<None>',
    description="(Optional) The base directory used for relative --log-file paths")

cinder.param(
    'use_syslog',
    type='boolean',
    default='false',
    description="Use syslog for logging.")

cinder.param(
    'syslog_log_facility',
    type='string',
    default='LOG_USER',
    description="syslog facility to receive log lines")

cinder.param(
    'default_notification_level',
    type='string',
    default='INFO',
    description="Default notification level for outgoing notifications")

cinder.param(
    'default_publisher_id',
    type='string',
    default='<None>',
    description="Default publisher_id for outgoing notifications")

cinder.param(
    'notification_topics',
    type='list',
    default='notifications',
    description="AMQP topic used for OpenStack notifications")

cinder.param(
    'topics',
    type='list',
    default='notifications',
    description="AMQP topic(s) used for OpenStack notifications")

cinder.param(
    'run_external_periodic_tasks',
    type='boolean',
    default='true',
    description="Some periodic tasks can be run in a separate process. Should we run them here?")

cinder.param(
    'rpc_backend',
    type='string',
    default='cinder.openstack.common.rpc.impl_kombu',
    description="The messaging module to use, defaults to kombu.")

cinder.param(
    'rpc_thread_pool_size',
    type='integer',
    default='64',
    description="Size of RPC thread pool")

cinder.param(
    'rpc_conn_pool_size',
    type='integer',
    default='30',
    description="Size of RPC connection pool")

cinder.param(
    'rpc_response_timeout',
    type='integer',
    default='60',
    description="Seconds to wait for a response from call or multicall")

cinder.param(
    'rpc_cast_timeout',
    type='integer',
    default='30',
    description="Seconds to wait before a cast expires")

cinder.param(
    'allowed_rpc_exception_modules',
    type='list',
    default='cinder.openstack.common.exception,nova.exception,cinder.exception,exceptions',
    description="Modules of exceptions that are permitted to be recreatedupon receiving exception data from an rpc call.")

cinder.param(
    'fake_rabbit',
    type='boolean',
    default='false',
    description="If passed, use a fake RabbitMQ provider")

cinder.param(
    'control_exchange',
    type='string',
    default='openstack',
    description="AMQP exchange to connect to if using RabbitMQ or Qpid")

cinder.param(
    'amqp_rpc_single_reply_queue',
    type='boolean',
    default='false',
    description="Enable a fast single reply queue if using AMQP based RPC like RabbitMQ or Qpid.")

cinder.param(
    'amqp_durable_queues',
    type='boolean',
    default='false',
    description="Use durable queues in amqp.")

cinder.param(
    'amqp_auto_delete',
    type='boolean',
    default='false',
    description="Auto-delete queues in amqp.")

cinder.param(
    'kombu_ssl_version',
    type='string',
    default='',
    description="SSL version to use")

cinder.param(
    'kombu_ssl_keyfile',
    type='string',
    default='',
    description="SSL key file")

cinder.param(
    'kombu_ssl_certfile',
    type='string',
    default='',
    description="SSL cert file")

cinder.param(
    'kombu_ssl_ca_certs',
    type='string',
    default='',
    description="SSL certification authority file")

cinder.param(
    'rabbit_host',
    type='string',
    default='localhost',
    description="The RabbitMQ broker address where a single node is used")

cinder.param(
    'rabbit_port',
    type='integer',
    default='5672',
    description="The RabbitMQ broker port where a single node is used")

cinder.param(
    'rabbit_hosts',
    type='list',
    default='$rabbit_host:$rabbit_port',
    description="RabbitMQ HA cluster host:port pairs")

cinder.param(
    'rabbit_use_ssl',
    type='boolean',
    default='false',
    description="connect over SSL for RabbitMQ")

cinder.param(
    'rabbit_userid',
    type='string',
    default='guest',
    description="the RabbitMQ userid")

cinder.param(
    'rabbit_password',
    type='string',
    default='guest',
    description="the RabbitMQ password")

cinder.param(
    'rabbit_virtual_host',
    type='string',
    default='/',
    description="the RabbitMQ virtual host")

cinder.param(
    'rabbit_retry_interval',
    type='integer',
    default='1',
    description="how frequently to retry connecting with RabbitMQ")

cinder.param(
    'rabbit_retry_backoff',
    type='integer',
    default='2',
    description="how long to backoff for between retries when connecting to RabbitMQ")

cinder.param(
    'rabbit_max_retries',
    type='integer',
    default='0',
    description="maximum retries with trying to connect to RabbitMQ")

cinder.param(
    'rabbit_ha_queues',
    type='boolean',
    default='false',
    description="use H/A queues in RabbitMQ")

cinder.param(
    'qpid_hostname',
    type='string',
    default='localhost',
    description="Qpid broker hostname")

cinder.param(
    'qpid_port',
    type='integer',
    default='5672',
    description="Qpid broker port")

cinder.param(
    'qpid_hosts',
    type='list',
    default='$qpid_hostname:$qpid_port',
    description="Qpid HA cluster host:port pairs")

cinder.param(
    'qpid_username',
    type='string',
    default='',
    description="Username for qpid connection")

cinder.param(
    'qpid_password',
    type='string',
    default='',
    description="Password for qpid connection")

cinder.param(
    'qpid_sasl_mechanisms',
    type='string',
    default='',
    description="Space separated list of SASL mechanisms to use for auth")

cinder.param(
    'qpid_heartbeat',
    type='integer',
    default='60',
    description="Seconds between connection keepalive heartbeats")

cinder.param(
    'qpid_protocol',
    type='string',
    default='tcp',
    description="Transport to use, either 'tcp' or 'ssl'")

cinder.param(
    'qpid_tcp_nodelay',
    type='boolean',
    default='true',
    description="Disable Nagle algorithm")

cinder.param(
    'qpid_topology_version',
    type='integer',
    default='1',
    description="The qpid topology version to use.  Version 1 is what was originally used by impl_qpid.  Version 2 includes some backwards-incompatible changes that allow broker federation to work.  Users should update to version 2 when they are able to take everything down, as it requires a clean break.")

cinder.param(
    'rpc_zmq_bind_address',
    type='string',
    default='*',
    description="ZeroMQ bind address. Should be a wildcard")

cinder.param(
    'rpc_zmq_matchmaker',
    type='string',
    default='cinder.openstack.common.rpc.matchmaker.MatchMakerLocalhost',
    description="MatchMaker driver")

cinder.param(
    'rpc_zmq_port',
    type='integer',
    default='9501',
    description="ZeroMQ receiver listening port")

cinder.param(
    'rpc_zmq_contexts',
    type='integer',
    default='1',
    description="Number of ZeroMQ contexts, defaults to 1")

cinder.param(
    'rpc_zmq_topic_backlog',
    type='integer',
    default='<None>',
    description="Maximum number of ingress messages to locally buffer per topic. Default is unlimited.")

cinder.param(
    'rpc_zmq_ipc_dir',
    type='string',
    default='/var/run/openstack',
    description="Directory for holding IPC sockets")

cinder.param(
    'rpc_zmq_host',
    type='string',
    default='cinder',
    description="Name of this node. Must be a valid hostname, FQDN, or IP address. Must match 'host' option, if running Nova.")

cinder.param(
    'matchmaker_ringfile',
    type='string',
    default='/etc/nova/matchmaker_ring.json',
    description="Matchmaker ring file")

cinder.param(
    'matchmaker_heartbeat_freq',
    type='integer',
    default='300',
    description="Heartbeat frequency")

cinder.param(
    'matchmaker_heartbeat_ttl',
    type='integer',
    default='600',
    description="Heartbeat time-to-live.")

cinder.param(
    'host',
    type='string',
    default='127.0.0.1',
    description="Host to locate redis")

cinder.param(
    'port',
    type='integer',
    default='6379',
    description="Use this port to connect to redis host.")

cinder.param(
    'password',
    type='string',
    default='<None>',
    description="Password for Redis server.")

cinder.param(
    'scheduler_host_manager',
    type='string',
    default='cinder.scheduler.host_manager.HostManager',
    description="The scheduler host manager class to use")

cinder.param(
    'scheduler_max_attempts',
    type='integer',
    default='3',
    description="Maximum number of attempts to schedule an volume")

cinder.param(
    'scheduler_default_filters',
    type='list',
    default='AvailabilityZoneFilter,CapacityFilter,CapabilitiesFilter',
    description="Which filter class names to use for filtering hosts when not specified in the request.")

cinder.param(
    'scheduler_default_weighers',
    type='list',
    default='CapacityWeigher',
    description="Which weigher class names to use for weighing hosts.")

cinder.param(
    'scheduler_driver',
    type='string',
    default='cinder.scheduler.filter_scheduler.FilterScheduler',
    description="Default scheduler driver to use")

cinder.param(
    'scheduler_json_config_location',
    type='string',
    default='',
    description="Absolute path to scheduler configuration JSON file.")

cinder.param(
    'max_gigabytes',
    type='integer',
    default='10000',
    description="maximum number of volume gigabytes to allow per host")

cinder.param(
    'capacity_weight_multiplier',
    type='floating point',
    default='1.0',
    description="Multiplier used for weighing volume capacity. Negative numbers mean to stack vs spread.")

cinder.param(
    'volume_transfer_salt_length',
    type='integer',
    default='8',
    description="The number of characters in the salt.")

cinder.param(
    'volume_transfer_key_length',
    type='integer',
    default='16',
    description="The number of characters in the autogenerated auth key.")

cinder.param(
    'snapshot_same_host',
    type='boolean',
    default='true',
    description="Create volume from snapshot at the host where snapshot resides")

cinder.param(
    'cloned_volume_same_az',
    type='boolean',
    default='true',
    description="Ensure that the new volumes are the same AZ as snapshot or source volume")

cinder.param(
    'num_shell_tries',
    type='integer',
    default='3',
    description="number of times to attempt to run flakey shell commands")

cinder.param(
    'reserved_percentage',
    type='integer',
    default='0',
    description="The percentage of backend capacity is reserved")

cinder.param(
    'iscsi_num_targets',
    type='integer',
    default='100',
    description="The maximum number of iscsi target ids per host")

cinder.param(
    'iscsi_target_prefix',
    type='string',
    default='iqn.2010-10.org.openstack:',
    description="prefix for iscsi volumes")

cinder.param(
    'iscsi_ip_address',
    type='string',
    default='$my_ip',
    description="The IP address that the iSCSI daemon is listening on")

cinder.param(
    'iscsi_port',
    type='integer',
    default='3260',
    description="The port that the iSCSI daemon is listening on")

cinder.param(
    'num_iser_scan_tries',
    type='integer',
    default='3',
    description="The maximum number of times to rescan iSER targetto find volume")

cinder.param(
    'iser_num_targets',
    type='integer',
    default='100',
    description="The maximum number of iser target ids per host")

cinder.param(
    'iser_target_prefix',
    type='string',
    default='iqn.2010-10.org.iser.openstack:',
    description="prefix for iser volumes")

cinder.param(
    'iser_ip_address',
    type='string',
    default='$my_ip',
    description="The IP address that the iSER daemon is listening on")

cinder.param(
    'iser_port',
    type='integer',
    default='3260',
    description="The port that the iSER daemon is listening on")

cinder.param(
    'volume_backend_name',
    type='string',
    default='<None>',
    description="The backend name for a given driver implementation")

cinder.param(
    'use_multipath_for_image_xfer',
    type='boolean',
    default='false',
    description="Do we attach/detach volumes in cinder using multipath for volume to image and image to volume transfers?")

cinder.param(
    'volume_clear',
    type='string',
    default='zero',
    description="Method used to wipe old voumes")

cinder.param(
    'volume_clear_size',
    type='integer',
    default='0',
    description="Size in MiB to wipe at start of old volumes. 0 => all")

cinder.param(
    'available_devices',
    type='list',
    default='',
    description="List of all available devices")

cinder.param(
    'coraid_esm_address',
    type='string',
    default='',
    description="IP address of Coraid ESM")

cinder.param(
    'coraid_user',
    type='string',
    default='admin',
    description="User name to connect to Coraid ESM")

cinder.param(
    'coraid_group',
    type='string',
    default='admin',
    description="Name of group on Coraid ESM to which coraid_user belongs")

cinder.param(
    'coraid_password',
    type='string',
    default='password',
    description="Password to connect to Coraid ESM")

cinder.param(
    'coraid_repository_key',
    type='string',
    default='coraid_repository',
    description="Volume Type key name to store ESM Repository Name")

cinder.param(
    'eqlx_group_name',
    type='string',
    default='group-0',
    description="Group name to use for creating volumes")

cinder.param(
    'eqlx_cli_timeout',
    type='integer',
    default='30',
    description="Timeout for the Group Manager cli command execution")

cinder.param(
    'eqlx_cli_max_retries',
    type='integer',
    default='5',
    description="Maximum retry count for reconnection")

cinder.param(
    'eqlx_use_chap',
    type='boolean',
    default='false',
    description="Use CHAP authentificaion for targets?")

cinder.param(
    'eqlx_chap_login',
    type='string',
    default='admin',
    description="Existing CHAP account name")

cinder.param(
    'eqlx_chap_password',
    type='string',
    default='password',
    description="Password for specified CHAP account name")

cinder.param(
    'eqlx_pool',
    type='string',
    default='default',
    description="Pool in which volumes will be created")

cinder.param(
    'glusterfs_shares_config',
    type='string',
    default='/etc/cinder/glusterfs_shares',
    description="File with the list of available gluster shares")

cinder.param(
    'glusterfs_disk_util',
    type='string',
    default='df',
    description="Use du or df for free space calculation")

cinder.param(
    'glusterfs_sparsed_volumes',
    type='boolean',
    default='true',
    description="Create volumes as sparsed files which take no space.If set to False volume is created as regular file.In such case volume creation takes a lot of time.")

cinder.param(
    'glusterfs_qcow2_volumes',
    type='boolean',
    default='false',
    description="Create volumes as QCOW2 files rather than raw files.")

cinder.param(
    'gpfs_mount_point_base',
    type='string',
    default='<None>',
    description="Path to the directory on GPFS mount point where volumes are stored")

cinder.param(
    'gpfs_images_dir',
    type='string',
    default='<None>',
    description="Path to GPFS Glance repository as mounted on Nova nodes")

cinder.param(
    'gpfs_images_share_mode',
    type='string',
    default='<None>',
    description="Set this if Glance image repo is on GPFS as well so that the image bits can be transferred efficiently between Glance and Cinder.  Valid values are copy or copy_on_write. copy performs a full copy of the image, copy_on_write efficiently shares unmodified blocks of the image.")

cinder.param(
    'gpfs_max_clone_depth',
    type='integer',
    default='0',
    description="A lengthy chain of copy-on-write snapshots or clones could have impact on performance.  This option limits the number of indirections required to reach a specific block. 0 indicates unlimited.")

cinder.param(
    'gpfs_sparse_volumes',
    type='boolean',
    default='true',
    description="Create volumes as sparse files which take no space. If set to False volume is created as regular file. In this case volume creation may take a significantly longer time.")

cinder.param(
    'hds_cinder_config_file',
    type='string',
    default='/opt/hds/hus/cinder_hus_conf.xml',
    description="configuration file for HDS cinder plugin for HUS")

cinder.param(
    'cinder_huawei_conf_file',
    type='string',
    default='/etc/cinder/cinder_huawei_conf.xml',
    description="config data for cinder huawei plugin")

cinder.param(
    'volume_group',
    type='string',
    default='cinder-volumes',
    description="Name for the VG that will contain exported volumes")

cinder.param(
    'pool_size',
    type='string',
    default='<None>',
    description="Size of thin provisioning pool")

cinder.param(
    'lvm_mirrors',
    type='integer',
    default='0',
    description="If set, create lvms with multiple mirrors. Note that this requires lvm_mirrors + 2 pvs with available space")

cinder.param(
    'lvm_type',
    type='string',
    default='default',
    description="Type of LVM volumes to deploy;")

cinder.param(
    'netapp_vfiler',
    type='string',
    default='<None>',
    description="Vfiler to use for provisioning")

cinder.param(
    'netapp_login',
    type='string',
    default='<None>',
    description="User name for the storage controller")

cinder.param(
    'netapp_password',
    type='string',
    default='<None>',
    description="Password for the storage controller")

cinder.param(
    'netapp_vserver',
    type='string',
    default='<None>',
    description="Cluster vserver to use for provisioning")

cinder.param(
    'netapp_server_hostname',
    type='string',
    default='<None>',
    description="Host name for the storage controller")

cinder.param(
    'netapp_server_port',
    type='integer',
    default='80',
    description="Port number for the storage controller")

cinder.param(
    'thres_avl_size_perc_start',
    type='integer',
    default='20',
    description="Threshold available percent to start cache cleaning.")

cinder.param(
    'thres_avl_size_perc_stop',
    type='integer',
    default='60',
    description="Threshold available percent to stop cache cleaning.")

cinder.param(
    'expiry_thres_minutes',
    type='integer',
    default='720',
    description="Threshold minutes after which cache file can be cleaned.")

cinder.param(
    'netapp_size_multiplier',
    type='floating point',
    default='1.2',
    description="Volume size multiplier to ensure while creation")

cinder.param(
    'netapp_volume_list',
    type='string',
    default='<None>',
    description="Comma separated volumes to be used for provisioning")

cinder.param(
    'netapp_storage_family',
    type='string',
    default='ontap_cluster',
    description="Storage family type.")

cinder.param(
    'netapp_storage_protocol',
    type='string',
    default='<None>',
    description="Storage protocol type.")

cinder.param(
    'netapp_transport_type',
    type='string',
    default='http',
    description="Transport type protocol")

cinder.param(
    'nexenta_host',
    type='string',
    default='',
    description="IP address of Nexenta SA")

cinder.param(
    'nexenta_rest_port',
    type='integer',
    default='2000',
    description="HTTP port to connect to Nexenta REST API server")

cinder.param(
    'nexenta_rest_protocol',
    type='string',
    default='auto',
    description="Use http or https for REST connection")

cinder.param(
    'nexenta_user',
    type='string',
    default='admin',
    description="User name to connect to Nexenta SA")

cinder.param(
    'nexenta_password',
    type='string',
    default='nexenta',
    description="Password to connect to Nexenta SA")

cinder.param(
    'nexenta_iscsi_target_portal_port',
    type='integer',
    default='3260',
    description="Nexenta target portal port")

cinder.param(
    'nexenta_volume',
    type='string',
    default='cinder',
    description="pool on SA that will hold all volumes")

cinder.param(
    'nexenta_target_prefix',
    type='string',
    default='iqn.1986-03.com.sun:02:cinder-',
    description="IQN prefix for iSCSI targets")

cinder.param(
    'nexenta_target_group_prefix',
    type='string',
    default='cinder/',
    description="prefix for iSCSI target groups on SA")

cinder.param(
    'nexenta_shares_config',
    type='string',
    default='/etc/cinder/nfs_shares',
    description="File with the list of available nfs shares")

cinder.param(
    'nexenta_mount_point_base',
    type='string',
    default='$state_path/mnt',
    description="Base dir containing mount points for nfs shares")

cinder.param(
    'nexenta_sparsed_volumes',
    type='boolean',
    default='true',
    description="Create volumes as sparsed files which take no space.If set to False volume is created as regular file.In such case volume creation takes a lot of time.")

cinder.param(
    'nexenta_volume_compression',
    type='string',
    default='on',
    description="Default compression value for new ZFS folders.")

cinder.param(
    'nexenta_mount_options',
    type='string',
    default='<None>',
    description="Mount options passed to the nfs client. See section of the nfs man page for details")

cinder.param(
    'nexenta_used_ratio',
    type='floating point',
    default='0.95',
    description="Percent of ACTUAL usage of the underlying volume before no new volumes can be allocated to the volume destination.")

cinder.param(
    'nexenta_oversub_ratio',
    type='floating point',
    default='1.0',
    description="This will compare the allocated to available space on the volume destination.  If the ratio exceeds this number, the destination will no longer be valid.")

cinder.param(
    'nexenta_blocksize',
    type='string',
    default='',
    description="block size for volumes")

cinder.param(
    'nexenta_sparse',
    type='boolean',
    default='false',
    description="flag to create sparse volumes")

cinder.param(
    'nfs_shares_config',
    type='string',
    default='/etc/cinder/nfs_shares',
    description="File with the list of available nfs shares")

cinder.param(
    'nfs_sparsed_volumes',
    type='boolean',
    default='true',
    description="Create volumes as sparsed files which take no space.If set to False volume is created as regular file.In such case volume creation takes a lot of time.")

cinder.param(
    'nfs_used_ratio',
    type='floating point',
    default='0.95',
    description="Percent of ACTUAL usage of the underlying volume before no new volumes can be allocated to the volume destination.")

cinder.param(
    'nfs_oversub_ratio',
    type='floating point',
    default='1.0',
    description="This will compare the allocated to available space on the volume destination.  If the ratio exceeds this number, the destination will no longer be valid.")

cinder.param(
    'rbd_pool',
    type='string',
    default='rbd',
    description="the RADOS pool in which rbd volumes are stored")

cinder.param(
    'rbd_user',
    type='string',
    default='<None>',
    description="the RADOS client name for accessing rbd volumes - only set when using cephx authentication")

cinder.param(
    'rbd_ceph_conf',
    type='string',
    default='',
    description="path to the ceph configuration file to use")

cinder.param(
    'rbd_flatten_volume_from_snapshot',
    type='boolean',
    default='false',
    description="flatten volumes created from snapshots to remove dependency")

cinder.param(
    'rbd_secret_uuid',
    type='string',
    default='<None>',
    description="the libvirt uuid of the secret for the rbd_uservolumes")

cinder.param(
    'volume_tmp_dir',
    type='string',
    default='<None>',
    description="where to store temporary image files if the volume driver does not write them directly to the volume")

cinder.param(
    'rbd_max_clone_depth',
    type='integer',
    default='5',
    description="maximum number of nested clones that can be taken of a volume before enforcing a flatten prior to next clone. A value of zero disables cloning")

cinder.param(
    'hp3par_api_url',
    type='string',
    default='',
    description="3PAR WSAPI Server Url like https://<3par ip>:8080/api/v1")

cinder.param(
    'hp3par_username',
    type='string',
    default='',
    description="3PAR Super user username")

cinder.param(
    'hp3par_password',
    type='string',
    default='',
    description="3PAR Super user password")

cinder.param(
    'hp3par_domain',
    type='string',
    default='<None>',
    description="This option is DEPRECATED and no longer used. The 3par domain name to use.")

cinder.param(
    'hp3par_cpg',
    type='string',
    default='OpenStack',
    description="The CPG to use for volume creation")

cinder.param(
    'hp3par_cpg_snap',
    type='string',
    default='',
    description="The CPG to use for Snapshots for volumes. If empty hp3par_cpg will be used")

cinder.param(
    'hp3par_snapshot_retention',
    type='string',
    default='',
    description="The time in hours to retain a snapshot.  You can't delete it before this expires.")

cinder.param(
    'hp3par_snapshot_expiration',
    type='string',
    default='',
    description="The time in hours when a snapshot expires  and is deleted. This must be larger than expiration")

cinder.param(
    'hp3par_debug',
    type='boolean',
    default='false',
    description="Enable HTTP debugging to 3PAR")

cinder.param(
    'hp3par_iscsi_ips',
    type='list',
    default='',
    description="List of target iSCSI addresses to use.")

cinder.param(
    'san_thin_provision',
    type='boolean',
    default='true',
    description="Use thin provisioning for SAN volumes?")

cinder.param(
    'san_ip',
    type='string',
    default='',
    description="IP address of SAN controller")

cinder.param(
    'san_login',
    type='string',
    default='admin',
    description="Username for SAN controller")

cinder.param(
    'san_password',
    type='string',
    default='',
    description="Password for SAN controller")

cinder.param(
    'san_private_key',
    type='string',
    default='',
    description="Filename of private key to use for SSH authentication")

cinder.param(
    'san_clustername',
    type='string',
    default='',
    description="Cluster name to use for creating volumes")

cinder.param(
    'san_ssh_port',
    type='integer',
    default='22',
    description="SSH port to use with SAN")

cinder.param(
    'san_is_local',
    type='boolean',
    default='false',
    description="Execute commands locally instead of over SSH; use if the volume service is running on the SAN device")

cinder.param(
    'ssh_conn_timeout',
    type='integer',
    default='30',
    description="SSH connection timeout in seconds")

cinder.param(
    'ssh_min_pool_conn',
    type='integer',
    default='1',
    description="Minimum ssh connections in the pool")

cinder.param(
    'ssh_max_pool_conn',
    type='integer',
    default='5',
    description="Maximum ssh connections in the pool")

cinder.param(
    'san_zfs_volume_base',
    type='string',
    default='rpool/',
    description="The ZFS path under which to create zvols for volumes.")

cinder.param(
    'scality_sofs_config',
    type='string',
    default='<None>',
    description="Path or URL to Scality SOFS configuration file")

cinder.param(
    'scality_sofs_mount_point',
    type='string',
    default='$state_path/scality',
    description="Base dir where Scality SOFS shall be mounted")

cinder.param(
    'scality_sofs_volume_dir',
    type='string',
    default='cinder/volumes',
    description="Path from Scality SOFS root to volume dir")

cinder.param(
    'sf_emulate_512',
    type='boolean',
    default='true',
    description="Set 512 byte emulation on volume creation; ")

cinder.param(
    'sf_allow_tenant_qos',
    type='boolean',
    default='false',
    description="Allow tenants to specify QOS on create")

cinder.param(
    'sf_account_prefix',
    type='string',
    default='cinder',
    description="Create SolidFire accounts with this prefix")

cinder.param(
    'sf_api_port',
    type='integer',
    default='443',
    description="SolidFire API port. Useful if the device api is behind a proxy on a different port.")

cinder.param(
    'storwize_svc_volpool_name',
    type='string',
    default='volpool',
    description="Storage system storage pool for volumes")

cinder.param(
    'storwize_svc_vol_rsize',
    type='integer',
    default='2',
    description="Storage system space-efficiency parameter for volumes")

cinder.param(
    'storwize_svc_vol_warning',
    type='integer',
    default='0',
    description="Storage system threshold for volume capacity warnings")

cinder.param(
    'storwize_svc_vol_autoexpand',
    type='boolean',
    default='true',
    description="Storage system autoexpand parameter for volumes")

cinder.param(
    'storwize_svc_vol_grainsize',
    type='integer',
    default='256',
    description="Storage system grain size parameter for volumes")

cinder.param(
    'storwize_svc_vol_compression',
    type='boolean',
    default='false',
    description="Storage system compression option for volumes")

cinder.param(
    'storwize_svc_vol_easytier',
    type='boolean',
    default='true',
    description="Enable Easy Tier for volumes")

cinder.param(
    'storwize_svc_vol_iogrp',
    type='integer',
    default='0',
    description="The I/O group in which to allocate volumes")

cinder.param(
    'storwize_svc_flashcopy_timeout',
    type='integer',
    default='120',
    description="Maximum number of seconds to wait for FlashCopy to be prepared. Maximum value is 600 seconds")

cinder.param(
    'storwize_svc_connection_protocol',
    type='string',
    default='iSCSI',
    description="Connection protocol")

cinder.param(
    'storwize_svc_multipath_enabled',
    type='boolean',
    default='false',
    description="Connect with multipath")

cinder.param(
    'storwize_svc_multihostmap_enabled',
    type='boolean',
    default='true',
    description="Allows vdisk to multi host mapping")

cinder.param(
    'vmware_host_ip',
    type='string',
    default='<None>',
    description="IP address for connecting to VMware ESX/VC server.")

cinder.param(
    'vmware_host_username',
    type='string',
    default='<None>',
    description="Username for authenticating with VMware ESX/VC server.")

cinder.param(
    'vmware_host_password',
    type='string',
    default='<None>',
    description="Password for authenticating with VMware ESX/VC server.")

cinder.param(
    'vmware_wsdl_location',
    type='string',
    default='<None>',
    description="Optional VIM service WSDL Location e.g http://<server>/vimService.wsdl. Optional over-ride to default location for bug work-arounds.")

cinder.param(
    'vmware_api_retry_count',
    type='integer',
    default='10',
    description="Number of times VMware ESX/VC server API must be retried upon connection related issues.")

cinder.param(
    'vmware_task_poll_interval',
    type='integer',
    default='5',
    description="The interval used for polling remote tasks invoked on VMware ESX/VC server.")

cinder.param(
    'vmware_volume_folder',
    type='string',
    default='cinder-volumes',
    description="Name for the folder in the VC datacenter that will contain cinder volumes.")

cinder.param(
    'vmware_image_transfer_timeout_secs',
    type='integer',
    default='7200',
    description="Timeout in seconds for VMDK volume transfer between Cinder and Glance.")

cinder.param(
    'windows_iscsi_lun_path',
    type='string',
    default='C:\iSCSIVirtualDisks',
    description="Path to store VHD backed volumes")

cinder.param(
    'xenapi_nfs_server',
    type='string',
    default='<None>',
    description="NFS server to be used by XenAPINFSDriver")

cinder.param(
    'xenapi_nfs_serverpath',
    type='string',
    default='<None>',
    description="Path of exported NFS, used by XenAPINFSDriver")

cinder.param(
    'xenapi_connection_url',
    type='string',
    default='<None>',
    description="URL for XenAPI connection")

cinder.param(
    'xenapi_connection_username',
    type='string',
    default='root',
    description="Username for XenAPI connection")

cinder.param(
    'xenapi_connection_password',
    type='string',
    default='<None>',
    description="Password for XenAPI connection")

cinder.param(
    'xenapi_sr_base_path',
    type='string',
    default='/var/run/sr-mount',
    description="Base path to the storage repository")

cinder.param(
    'xiv_ds8k_proxy',
    type='string',
    default='xiv_ds8k_openstack.nova_proxy.XIVDS8KNovaProxy',
    description="Proxy driver that connects to the IBM Storage Array")

cinder.param(
    'xiv_ds8k_connection_type',
    type='string',
    default='iscsi',
    description="Connection type to the IBM Storage Array")

cinder.param(
    'zadara_vpsa_ip',
    type='string',
    default='<None>',
    description="Management IP of Zadara VPSA")

cinder.param(
    'zadara_vpsa_port',
    type='string',
    default='<None>',
    description="Zadara VPSA port number")

cinder.param(
    'zadara_vpsa_use_ssl',
    type='boolean',
    default='false',
    description="Use SSL connection")

cinder.param(
    'zadara_user',
    type='string',
    default='<None>',
    description="User name for the VPSA")

cinder.param(
    'zadara_password',
    type='string',
    default='<None>',
    description="Password for the VPSA")

cinder.param(
    'zadara_vpsa_poolname',
    type='string',
    default='<None>',
    description="Name of VPSA storage pool for volumes")

cinder.param(
    'zadara_vol_thin',
    type='boolean',
    default='true',
    description="Default thin provisioning policy for volumes")

cinder.param(
    'zadara_vol_encrypt',
    type='boolean',
    default='false',
    description="Default encryption policy for volumes")

cinder.param(
    'zadara_default_striping_mode',
    type='string',
    default='simple',
    description="Default striping mode for volumes")

cinder.param(
    'zadara_default_stripesize',
    type='string',
    default='64',
    description="Default stripe size for volumes")

cinder.param(
    'zadara_vol_name_template',
    type='string',
    default='OS_%s',
    description="Default template for VPSA volume names")

cinder.param(
    'zadara_vpsa_auto_detach_on_delete',
    type='boolean',
    default='true',
    description="Automatically detach from servers on volume delete")

cinder.param(
    'zadara_vpsa_allow_nonexistent_delete',
    type='boolean',
    default='true',
    description="Don't halt on deletion of non-existing volumes")

cinder.param(
    'volume_driver',
    type='string',
    default='cinder.volume.drivers.lvm.LVMISCSIDriver',
    description="Driver to use for volume creation")

cinder.param(
    'migration_create_volume_timeout_secs',
    type='integer',
    default='300',
    description="Timeout for creating the volume to migrate to when performing volume migration")

cinder.param(
    'volume_dd_blocksize',
    type='string',
    default='1M',
    description="The default block size used when copying/clearing volumes")

cinder.commit()
