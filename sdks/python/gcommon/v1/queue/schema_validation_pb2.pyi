from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SchemaValidation(_message.Message):
    __slots__ = ("passed", "backup_schema_version", "current_schema_version", "compatibility_status")
    PASSED_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    passed: bool
    backup_schema_version: str
    current_schema_version: str
    compatibility_status: str
    def __init__(self, passed: bool = ..., backup_schema_version: _Optional[str] = ..., current_schema_version: _Optional[str] = ..., compatibility_status: _Optional[str] = ...) -> None: ...
