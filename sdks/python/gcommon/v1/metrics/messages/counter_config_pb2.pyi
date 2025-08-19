from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CounterConfig(_message.Message):
    __slots__ = ("initial_value", "allow_reset", "max_value")
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RESET_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    initial_value: float
    allow_reset: bool
    max_value: float
    def __init__(self, initial_value: _Optional[float] = ..., allow_reset: bool = ..., max_value: _Optional[float] = ...) -> None: ...
