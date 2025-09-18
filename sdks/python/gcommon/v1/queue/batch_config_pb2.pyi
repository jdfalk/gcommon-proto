import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchConfig(_message.Message):
    __slots__ = ("max_batch_size", "max_wait_time", "max_batch_bytes", "enable_compression", "worker_count", "buffer_size")
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_BYTES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    max_batch_size: int
    max_wait_time: _duration_pb2.Duration
    max_batch_bytes: int
    enable_compression: bool
    worker_count: int
    buffer_size: int
    def __init__(self, max_batch_size: _Optional[int] = ..., max_wait_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., max_batch_bytes: _Optional[int] = ..., enable_compression: _Optional[bool] = ..., worker_count: _Optional[int] = ..., buffer_size: _Optional[int] = ...) -> None: ...
