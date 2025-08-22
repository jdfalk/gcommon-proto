from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateSubtitlesResponse(_message.Message):
    __slots__ = ("is_valid", "validation_errors", "validation_warnings", "detected_format")
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    DETECTED_FORMAT_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    validation_errors: _containers.RepeatedScalarFieldContainer[str]
    validation_warnings: _containers.RepeatedScalarFieldContainer[str]
    detected_format: str
    def __init__(self, is_valid: bool = ..., validation_errors: _Optional[_Iterable[str]] = ..., validation_warnings: _Optional[_Iterable[str]] = ..., detected_format: _Optional[str] = ...) -> None: ...
