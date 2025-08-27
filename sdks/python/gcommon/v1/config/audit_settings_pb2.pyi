from gcommon.v1.common import audit_level_pb2 as _audit_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditSettings(_message.Message):
    __slots__ = ("enabled", "level", "retention_days", "include_sensitive_data", "destinations", "format", "metadata")
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
    INCLUDE_SENSITIVE_DATA_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    level: _audit_level_pb2.AuditLevel
    retention_days: int
    include_sensitive_data: bool
    destinations: _containers.RepeatedScalarFieldContainer[str]
    format: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: _Optional[bool] = ..., level: _Optional[_Union[_audit_level_pb2.AuditLevel, str]] = ..., retention_days: _Optional[int] = ..., include_sensitive_data: _Optional[bool] = ..., destinations: _Optional[_Iterable[str]] = ..., format: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
