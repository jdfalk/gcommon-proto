from gcommon.v1.common import aggregation_type_pb2 as _aggregation_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricAggregation(_message.Message):
    __slots__ = ("type", "window_seconds", "group_by", "percentiles", "custom_function", "include_nulls", "min_samples")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    PERCENTILES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NULLS_FIELD_NUMBER: _ClassVar[int]
    MIN_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    type: _aggregation_type_pb2.AggregationType
    window_seconds: int
    group_by: _containers.RepeatedScalarFieldContainer[str]
    percentiles: _containers.RepeatedScalarFieldContainer[float]
    custom_function: str
    include_nulls: bool
    min_samples: int
    def __init__(self, type: _Optional[_Union[_aggregation_type_pb2.AggregationType, str]] = ..., window_seconds: _Optional[int] = ..., group_by: _Optional[_Iterable[str]] = ..., percentiles: _Optional[_Iterable[float]] = ..., custom_function: _Optional[str] = ..., include_nulls: _Optional[bool] = ..., min_samples: _Optional[int] = ...) -> None: ...
