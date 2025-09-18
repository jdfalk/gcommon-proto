from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorTrend(_message.Message):
    __slots__ = ("error_rate_trend", "trend_confidence", "emerging_error_types")
    ERROR_RATE_TREND_FIELD_NUMBER: _ClassVar[int]
    TREND_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    EMERGING_ERROR_TYPES_FIELD_NUMBER: _ClassVar[int]
    error_rate_trend: str
    trend_confidence: float
    emerging_error_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, error_rate_trend: _Optional[str] = ..., trend_confidence: _Optional[float] = ..., emerging_error_types: _Optional[_Iterable[str]] = ...) -> None: ...
