from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LabelDefinition(_message.Message):
    __slots__ = ("name", "description", "required", "allowed_values", "validation_pattern", "default_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    required: bool
    allowed_values: _containers.RepeatedScalarFieldContainer[str]
    validation_pattern: str
    default_value: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., required: bool = ..., allowed_values: _Optional[_Iterable[str]] = ..., validation_pattern: _Optional[str] = ..., default_value: _Optional[str] = ...) -> None: ...
