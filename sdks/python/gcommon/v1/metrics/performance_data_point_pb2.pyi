from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceDataPoint(_message.Message):
    __slots__ = ("timestamp", "ops_per_second", "latency_ms", "throughput_bytes_per_second")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    OPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    ops_per_second: float
    latency_ms: float
    throughput_bytes_per_second: float
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ops_per_second: _Optional[float] = ..., latency_ms: _Optional[float] = ..., throughput_bytes_per_second: _Optional[float] = ...) -> None: ...
