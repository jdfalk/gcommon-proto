from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PerformanceTrend(_message.Message):
    __slots__ = ("latency_trend", "throughput_trend", "trend_confidence")
    LATENCY_TREND_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_TREND_FIELD_NUMBER: _ClassVar[int]
    TREND_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    latency_trend: str
    throughput_trend: str
    trend_confidence: float
    def __init__(
        self,
        latency_trend: _Optional[str] = ...,
        throughput_trend: _Optional[str] = ...,
        trend_confidence: _Optional[float] = ...,
    ) -> None: ...
