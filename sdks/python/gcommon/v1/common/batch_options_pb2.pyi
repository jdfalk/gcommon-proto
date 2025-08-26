import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonBatchOptions(_message.Message):
    __slots__ = ("max_parallel", "fail_fast", "timeout", "return_partial")
    MAX_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    FAIL_FAST_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETURN_PARTIAL_FIELD_NUMBER: _ClassVar[int]
    max_parallel: int
    fail_fast: bool
    timeout: _duration_pb2.Duration
    return_partial: bool
    def __init__(self, max_parallel: _Optional[int] = ..., fail_fast: _Optional[bool] = ..., timeout: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., return_partial: _Optional[bool] = ...) -> None: ...
