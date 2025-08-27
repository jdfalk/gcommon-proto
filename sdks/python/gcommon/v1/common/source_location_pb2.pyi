from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SourceLocation(_message.Message):
    __slots__ = ("file", "line", "function", "package")
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    file: str
    line: int
    function: str
    package: str
    def __init__(
        self,
        file: _Optional[str] = ...,
        line: _Optional[int] = ...,
        function: _Optional[str] = ...,
        package: _Optional[str] = ...,
    ) -> None: ...
