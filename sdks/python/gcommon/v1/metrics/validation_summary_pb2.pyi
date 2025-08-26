from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationSummary(_message.Message):
    __slots__ = ("valid_count", "invalid_count", "common_errors", "schema_version")
    VALID_COUNT_FIELD_NUMBER: _ClassVar[int]
    INVALID_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMMON_ERRORS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    valid_count: int
    invalid_count: int
    common_errors: _containers.RepeatedScalarFieldContainer[str]
    schema_version: str
    def __init__(self, valid_count: _Optional[int] = ..., invalid_count: _Optional[int] = ..., common_errors: _Optional[_Iterable[str]] = ..., schema_version: _Optional[str] = ...) -> None: ...
