from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataVolumeTrend(_message.Message):
    __slots__ = ("volume_trend", "ingestion_trend", "trend_confidence")
    VOLUME_TREND_FIELD_NUMBER: _ClassVar[int]
    INGESTION_TREND_FIELD_NUMBER: _ClassVar[int]
    TREND_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    volume_trend: str
    ingestion_trend: str
    trend_confidence: float
    def __init__(self, volume_trend: _Optional[str] = ..., ingestion_trend: _Optional[str] = ..., trend_confidence: _Optional[float] = ...) -> None: ...
