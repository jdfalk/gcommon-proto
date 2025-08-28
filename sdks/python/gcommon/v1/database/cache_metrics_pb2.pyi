from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheMetrics(_message.Message):
    __slots__ = ("ops_per_second", "reads_per_second", "writes_per_second", "avg_response_time", "p95_response_time", "p99_response_time", "total_connections", "active_connections", "network_bytes_in", "network_bytes_out", "cpu_usage_percent", "memory_usage_percent", "collected_at")
    OPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    READS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    WRITES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    AVG_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    P95_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    P99_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_IN_FIELD_NUMBER: _ClassVar[int]
    NETWORK_BYTES_OUT_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    COLLECTED_AT_FIELD_NUMBER: _ClassVar[int]
    ops_per_second: float
    reads_per_second: float
    writes_per_second: float
    avg_response_time: _duration_pb2.Duration
    p95_response_time: _duration_pb2.Duration
    p99_response_time: _duration_pb2.Duration
    total_connections: int
    active_connections: int
    network_bytes_in: int
    network_bytes_out: int
    cpu_usage_percent: float
    memory_usage_percent: float
    collected_at: _timestamp_pb2.Timestamp
    def __init__(self, ops_per_second: _Optional[float] = ..., reads_per_second: _Optional[float] = ..., writes_per_second: _Optional[float] = ..., avg_response_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., p95_response_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., p99_response_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., total_connections: _Optional[int] = ..., active_connections: _Optional[int] = ..., network_bytes_in: _Optional[int] = ..., network_bytes_out: _Optional[int] = ..., cpu_usage_percent: _Optional[float] = ..., memory_usage_percent: _Optional[float] = ..., collected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
