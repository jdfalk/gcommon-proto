from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueBackupConfig(_message.Message):
    __slots__ = ("interval", "retention", "location", "enabled")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    interval: _duration_pb2.Duration
    retention: _duration_pb2.Duration
    location: str
    enabled: bool
    def __init__(self, interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retention: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., location: _Optional[str] = ..., enabled: bool = ...) -> None: ...
