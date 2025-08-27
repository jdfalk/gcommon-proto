from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsBatchStats(_message.Message):
    __slots__ = ("total_processing_time_ms", "avg_processing_time_ms", "total_data_size_bytes", "deduplication_count", "parallel_workers", "storage_latency_ms", "memory_usage_bytes")
    TOTAL_PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    AVG_PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_WORKERS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_processing_time_ms: int
    avg_processing_time_ms: int
    total_data_size_bytes: int
    deduplication_count: int
    parallel_workers: int
    storage_latency_ms: int
    memory_usage_bytes: int
    def __init__(self, total_processing_time_ms: _Optional[int] = ..., avg_processing_time_ms: _Optional[int] = ..., total_data_size_bytes: _Optional[int] = ..., deduplication_count: _Optional[int] = ..., parallel_workers: _Optional[int] = ..., storage_latency_ms: _Optional[int] = ..., memory_usage_bytes: _Optional[int] = ...) -> None: ...
