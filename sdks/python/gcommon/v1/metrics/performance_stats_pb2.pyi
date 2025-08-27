from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsPerformanceStats(_message.Message):
    __slots__ = ("avg_response_time_ms", "max_response_time_ms", "min_response_time_ms", "p95_response_time_ms", "p99_response_time_ms", "requests_per_second", "total_requests", "successful_requests", "failed_requests", "success_rate", "cpu_utilization", "memory_utilization", "network_io_bytes_per_sec", "disk_io_bytes_per_sec")
    AVG_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    MIN_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    P95_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    P99_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TOTAL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    FAILED_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    CPU_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    MEMORY_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_IO_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    DISK_IO_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    avg_response_time_ms: float
    max_response_time_ms: float
    min_response_time_ms: float
    p95_response_time_ms: float
    p99_response_time_ms: float
    requests_per_second: float
    total_requests: int
    successful_requests: int
    failed_requests: int
    success_rate: float
    cpu_utilization: float
    memory_utilization: float
    network_io_bytes_per_sec: float
    disk_io_bytes_per_sec: float
    def __init__(self, avg_response_time_ms: _Optional[float] = ..., max_response_time_ms: _Optional[float] = ..., min_response_time_ms: _Optional[float] = ..., p95_response_time_ms: _Optional[float] = ..., p99_response_time_ms: _Optional[float] = ..., requests_per_second: _Optional[float] = ..., total_requests: _Optional[int] = ..., successful_requests: _Optional[int] = ..., failed_requests: _Optional[int] = ..., success_rate: _Optional[float] = ..., cpu_utilization: _Optional[float] = ..., memory_utilization: _Optional[float] = ..., network_io_bytes_per_sec: _Optional[float] = ..., disk_io_bytes_per_sec: _Optional[float] = ...) -> None: ...
