import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueConfiguration(_message.Message):
    __slots__ = ("max_messages", "visibility_timeout", "message_retention_period", "max_retry_attempts", "dead_letter_queue_enabled")
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_QUEUE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    max_messages: int
    visibility_timeout: _duration_pb2.Duration
    message_retention_period: _duration_pb2.Duration
    max_retry_attempts: int
    dead_letter_queue_enabled: bool
    def __init__(self, max_messages: _Optional[int] = ..., visibility_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., message_retention_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_retry_attempts: _Optional[int] = ..., dead_letter_queue_enabled: _Optional[bool] = ...) -> None: ...
