from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceReference(_message.Message):
    __slots__ = ("type", "id", "name", "module")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    type: str
    id: str
    name: str
    module: str
    def __init__(self, type: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., module: _Optional[str] = ...) -> None: ...
