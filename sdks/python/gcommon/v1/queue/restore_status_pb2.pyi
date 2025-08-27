import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreStatus(_message.Message):
    __slots__ = ("status_code", "status_message", "progress_percentage", "current_phase", "estimated_remaining", "last_update")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PHASE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_REMAINING_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    status_code: str
    status_message: str
    progress_percentage: int
    current_phase: str
    estimated_remaining: _duration_pb2.Duration
    last_update: _timestamp_pb2.Timestamp
    def __init__(self, status_code: _Optional[str] = ..., status_message: _Optional[str] = ..., progress_percentage: _Optional[int] = ..., current_phase: _Optional[str] = ..., estimated_remaining: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., last_update: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
