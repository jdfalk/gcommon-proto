from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorNotificationConfig(_message.Message):
    __slots__ = ("enabled", "notification_channels", "error_threshold", "notification_frequency_seconds")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    ERROR_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FREQUENCY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    notification_channels: _containers.RepeatedScalarFieldContainer[str]
    error_threshold: int
    notification_frequency_seconds: int
    def __init__(self, enabled: bool = ..., notification_channels: _Optional[_Iterable[str]] = ..., error_threshold: _Optional[int] = ..., notification_frequency_seconds: _Optional[int] = ...) -> None: ...
