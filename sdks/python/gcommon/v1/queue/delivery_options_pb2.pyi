import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryOptions(_message.Message):
    __slots__ = ("delay", "max_retries", "retry_delay", "backoff_multiplier", "max_retry_delay", "dead_letter_queue", "require_ack", "ack_timeout")
    DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRY_DELAY_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_QUEUE_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_ACK_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    delay: _duration_pb2.Duration
    max_retries: int
    retry_delay: _duration_pb2.Duration
    backoff_multiplier: float
    max_retry_delay: _duration_pb2.Duration
    dead_letter_queue: str
    require_ack: bool
    ack_timeout: _duration_pb2.Duration
    def __init__(self, delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_retries: _Optional[int] = ..., retry_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., backoff_multiplier: _Optional[float] = ..., max_retry_delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., dead_letter_queue: _Optional[str] = ..., require_ack: _Optional[bool] = ..., ack_timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
