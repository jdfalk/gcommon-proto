from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUsageTrend(_message.Message):
    __slots__ = ("memory_trend", "cpu_trend", "disk_trend", "trend_confidence")
    MEMORY_TREND_FIELD_NUMBER: _ClassVar[int]
    CPU_TREND_FIELD_NUMBER: _ClassVar[int]
    DISK_TREND_FIELD_NUMBER: _ClassVar[int]
    TREND_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    memory_trend: str
    cpu_trend: str
    disk_trend: str
    trend_confidence: float
    def __init__(self, memory_trend: _Optional[str] = ..., cpu_trend: _Optional[str] = ..., disk_trend: _Optional[str] = ..., trend_confidence: _Optional[float] = ...) -> None: ...
