from gcommon.v1.config.enums import deprecation_level_pb2 as _deprecation_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeprecationInfo(_message.Message):
    __slots__ = ("deprecated", "reason", "deprecated_at", "replacement_key", "removal_date", "migration_guide", "level")
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_KEY_FIELD_NUMBER: _ClassVar[int]
    REMOVAL_DATE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_GUIDE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    deprecated: bool
    reason: str
    deprecated_at: _timestamp_pb2.Timestamp
    replacement_key: str
    removal_date: _timestamp_pb2.Timestamp
    migration_guide: str
    level: _deprecation_level_pb2.DeprecationLevel
    def __init__(self, deprecated: bool = ..., reason: _Optional[str] = ..., deprecated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., replacement_key: _Optional[str] = ..., removal_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., migration_guide: _Optional[str] = ..., level: _Optional[_Union[_deprecation_level_pb2.DeprecationLevel, str]] = ...) -> None: ...
