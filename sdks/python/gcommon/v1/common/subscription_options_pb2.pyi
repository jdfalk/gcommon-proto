import datetime

from gcommon.v1.common import ack_mode_pb2 as _ack_mode_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionOptions(_message.Message):
    __slots__ = ("include_history", "max_batch_size", "ack_mode", "keep_alive")
    INCLUDE_HISTORY_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    ACK_MODE_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    include_history: bool
    max_batch_size: int
    ack_mode: _ack_mode_pb2.AckMode
    keep_alive: _duration_pb2.Duration
    def __init__(self, include_history: _Optional[bool] = ..., max_batch_size: _Optional[int] = ..., ack_mode: _Optional[_Union[_ack_mode_pb2.AckMode, str]] = ..., keep_alive: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
