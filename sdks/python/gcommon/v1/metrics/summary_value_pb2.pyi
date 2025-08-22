from gcommon.v1.metrics import quantile_pb2 as _quantile_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SummaryValue(_message.Message):
    __slots__ = ("quantiles", "count", "sum")
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    quantiles: _containers.RepeatedCompositeFieldContainer[_quantile_pb2.Quantile]
    count: int
    sum: float
    def __init__(self, quantiles: _Optional[_Iterable[_Union[_quantile_pb2.Quantile, _Mapping]]] = ..., count: _Optional[int] = ..., sum: _Optional[float] = ...) -> None: ...
