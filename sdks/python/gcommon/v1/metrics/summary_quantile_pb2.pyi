from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SummaryQuantile(_message.Message):
    __slots__ = ("quantile", "value")
    QUANTILE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    quantile: float
    value: float
    def __init__(self, quantile: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...
