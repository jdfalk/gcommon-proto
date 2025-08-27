from gcommon.v1.common import error_type_count_pb2 as _error_type_count_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsErrorStats(_message.Message):
    __slots__ = ("total_errors", "error_rate", "error_types", "error_trend")
    TOTAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPES_FIELD_NUMBER: _ClassVar[int]
    ERROR_TREND_FIELD_NUMBER: _ClassVar[int]
    total_errors: int
    error_rate: float
    error_types: _containers.RepeatedCompositeFieldContainer[
        _error_type_count_pb2.ErrorTypeCount
    ]
    error_trend: str
    def __init__(
        self,
        total_errors: _Optional[int] = ...,
        error_rate: _Optional[float] = ...,
        error_types: _Optional[
            _Iterable[_Union[_error_type_count_pb2.ErrorTypeCount, _Mapping]]
        ] = ...,
        error_trend: _Optional[str] = ...,
    ) -> None: ...
