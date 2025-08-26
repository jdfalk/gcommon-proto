from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuditAlert(_message.Message):
    __slots__ = ("name", "event_patterns", "severity", "notification_channels", "threshold", "time_window_minutes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_PATTERNS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOW_MINUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    event_patterns: _containers.RepeatedScalarFieldContainer[str]
    severity: str
    notification_channels: _containers.RepeatedScalarFieldContainer[str]
    threshold: int
    time_window_minutes: int
    def __init__(self, name: _Optional[str] = ..., event_patterns: _Optional[_Iterable[str]] = ..., severity: _Optional[str] = ..., notification_channels: _Optional[_Iterable[str]] = ..., threshold: _Optional[int] = ..., time_window_minutes: _Optional[int] = ...) -> None: ...
