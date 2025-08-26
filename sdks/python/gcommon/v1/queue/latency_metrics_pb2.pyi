from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LatencyMetrics(_message.Message):
    __slots__ = ("p50_processing_latency_ms", "p95_processing_latency_ms", "p99_processing_latency_ms", "average_queue_latency_ms", "p95_queue_latency_ms", "average_e2e_latency_ms", "p95_e2e_latency_ms")
    P50_PROCESSING_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    P95_PROCESSING_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    P99_PROCESSING_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_QUEUE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    P95_QUEUE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_E2E_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    P95_E2E_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    p50_processing_latency_ms: float
    p95_processing_latency_ms: float
    p99_processing_latency_ms: float
    average_queue_latency_ms: float
    p95_queue_latency_ms: float
    average_e2e_latency_ms: float
    p95_e2e_latency_ms: float
    def __init__(self, p50_processing_latency_ms: _Optional[float] = ..., p95_processing_latency_ms: _Optional[float] = ..., p99_processing_latency_ms: _Optional[float] = ..., average_queue_latency_ms: _Optional[float] = ..., p95_queue_latency_ms: _Optional[float] = ..., average_e2e_latency_ms: _Optional[float] = ..., p95_e2e_latency_ms: _Optional[float] = ...) -> None: ...
