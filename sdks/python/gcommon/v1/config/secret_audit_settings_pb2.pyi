from gcommon.v1.common import secret_audit_level_pb2 as _secret_audit_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecretAuditSettings(_message.Message):
    __slots__ = ("enabled", "level", "retention_days", "log_access", "log_rotation", "log_modification", "destinations", "format", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    LOG_ACCESS_FIELD_NUMBER: _ClassVar[int]
    LOG_ROTATION_FIELD_NUMBER: _ClassVar[int]
    LOG_MODIFICATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    level: _secret_audit_level_pb2.SecretAuditLevel
    retention_days: int
    log_access: bool
    log_rotation: bool
    log_modification: bool
    destinations: _containers.RepeatedScalarFieldContainer[str]
    format: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., level: _Optional[_Union[_secret_audit_level_pb2.SecretAuditLevel, str]] = ..., retention_days: _Optional[int] = ..., log_access: bool = ..., log_rotation: bool = ..., log_modification: bool = ..., destinations: _Optional[_Iterable[str]] = ..., format: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
