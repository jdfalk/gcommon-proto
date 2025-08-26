from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SummaryConfig(_message.Message):
    __slots__ = ("quantiles", "time_window", "max_age")
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    quantiles: _containers.RepeatedScalarFieldContainer[float]
    time_window: str
    max_age: str
    def __init__(self, quantiles: _Optional[_Iterable[float]] = ..., time_window: _Optional[str] = ..., max_age: _Optional[str] = ...) -> None: ...
