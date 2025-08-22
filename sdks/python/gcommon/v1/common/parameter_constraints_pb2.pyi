from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ParameterConstraints(_message.Message):
    __slots__ = ("min_value", "max_value", "pattern", "required", "default_value")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    min_value: str
    max_value: str
    pattern: str
    required: bool
    default_value: str
    def __init__(self, min_value: _Optional[str] = ..., max_value: _Optional[str] = ..., pattern: _Optional[str] = ..., required: bool = ..., default_value: _Optional[str] = ...) -> None: ...
