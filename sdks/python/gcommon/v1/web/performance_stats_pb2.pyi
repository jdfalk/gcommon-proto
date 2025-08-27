from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WebPerformanceStats(_message.Message):
    __slots__ = (
        "request_count",
        "average_latency_ms",
        "active_connections",
        "error_rate",
    )
    REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    request_count: int
    average_latency_ms: float
    active_connections: int
    error_rate: float
    def __init__(
        self,
        request_count: _Optional[int] = ...,
        average_latency_ms: _Optional[float] = ...,
        active_connections: _Optional[int] = ...,
        error_rate: _Optional[float] = ...,
    ) -> None: ...
