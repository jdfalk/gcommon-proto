from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GaugeConfig(_message.Message):
    __slots__ = ("min_value", "max_value", "allow_negative")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    min_value: float
    max_value: float
    allow_negative: bool
    def __init__(self, min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., allow_negative: _Optional[bool] = ...) -> None: ...
