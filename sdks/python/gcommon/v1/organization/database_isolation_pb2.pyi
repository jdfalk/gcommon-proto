from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.organization import backup_config_pb2 as _backup_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseIsolation(_message.Message):
    __slots__ = ("database_instance", "schema_name", "connection_params", "dedicated_database", "backup", "allowed_operations", "max_connections", "query_timeout_seconds")
    DATABASE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_DATABASE_FIELD_NUMBER: _ClassVar[int]
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    database_instance: str
    schema_name: str
    connection_params: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    dedicated_database: bool
    backup: _backup_config_pb2.OrganizationBackupConfig
    allowed_operations: _containers.RepeatedScalarFieldContainer[str]
    max_connections: int
    query_timeout_seconds: int
    def __init__(self, database_instance: _Optional[str] = ..., schema_name: _Optional[str] = ..., connection_params: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., dedicated_database: bool = ..., backup: _Optional[_Union[_backup_config_pb2.OrganizationBackupConfig, _Mapping]] = ..., allowed_operations: _Optional[_Iterable[str]] = ..., max_connections: _Optional[int] = ..., query_timeout_seconds: _Optional[int] = ...) -> None: ...
