from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrationScript(_message.Message):
    __slots__ = ("version", "script", "description")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    version: str
    script: str
    description: str
    def __init__(
        self,
        version: _Optional[str] = ...,
        script: _Optional[str] = ...,
        description: _Optional[str] = ...,
    ) -> None: ...
