import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchExecuteOptions(_message.Message):
    __slots__ = ("fail_fast", "timeout", "max_parallel")
    FAIL_FAST_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    fail_fast: bool
    timeout: _duration_pb2.Duration
    max_parallel: int
    def __init__(self, fail_fast: _Optional[bool] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_parallel: _Optional[int] = ...) -> None: ...
