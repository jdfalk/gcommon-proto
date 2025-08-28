from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigRetentionPolicy(_message.Message):
    __slots__ = ("enabled", "config_retention_days", "audit_retention_days", "backup_retention_days", "metrics_retention_days", "custom_retention")
    class CustomRetentionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    AUDIT_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    METRICS_RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RETENTION_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    config_retention_days: int
    audit_retention_days: int
    backup_retention_days: int
    metrics_retention_days: int
    custom_retention: _containers.ScalarMap[str, int]
    def __init__(self, enabled: bool = ..., config_retention_days: _Optional[int] = ..., audit_retention_days: _Optional[int] = ..., backup_retention_days: _Optional[int] = ..., metrics_retention_days: _Optional[int] = ..., custom_retention: _Optional[_Mapping[str, int]] = ...) -> None: ...
