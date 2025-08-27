from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaConfig(_message.Message):
    __slots__ = ("version", "definition", "type", "validate")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    version: int
    definition: str
    type: str
    validate: bool
    def __init__(self, version: _Optional[int] = ..., definition: _Optional[str] = ..., type: _Optional[str] = ..., validate: _Optional[bool] = ...) -> None: ...
