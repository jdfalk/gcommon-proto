from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationRules(_message.Message):
    __slots__ = ("min_value", "max_value", "allow_null", "validation_expressions")
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NULL_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    min_value: float
    max_value: float
    allow_null: bool
    validation_expressions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., allow_null: bool = ..., validation_expressions: _Optional[_Iterable[str]] = ...) -> None: ...
