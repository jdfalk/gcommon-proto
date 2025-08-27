import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceConfig(_message.Message):
    __slots__ = (
        "buffer_size",
        "max_batch_size",
        "flush_interval",
        "worker_threads",
        "queue_capacity",
        "async_processing",
        "connection_pool_size",
        "max_idle_time",
        "enable_multiplexing",
        "read_timeout",
        "write_timeout",
    )
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    FLUSH_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    WORKER_THREADS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ASYNC_PROCESSING_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_IDLE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MULTIPLEXING_FIELD_NUMBER: _ClassVar[int]
    READ_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WRITE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    buffer_size: int
    max_batch_size: int
    flush_interval: _duration_pb2.Duration
    worker_threads: int
    queue_capacity: int
    async_processing: bool
    connection_pool_size: int
    max_idle_time: _duration_pb2.Duration
    enable_multiplexing: bool
    read_timeout: _duration_pb2.Duration
    write_timeout: _duration_pb2.Duration
    def __init__(
        self,
        buffer_size: _Optional[int] = ...,
        max_batch_size: _Optional[int] = ...,
        flush_interval: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        worker_threads: _Optional[int] = ...,
        queue_capacity: _Optional[int] = ...,
        async_processing: _Optional[bool] = ...,
        connection_pool_size: _Optional[int] = ...,
        max_idle_time: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        enable_multiplexing: _Optional[bool] = ...,
        read_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        write_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
    ) -> None: ...
