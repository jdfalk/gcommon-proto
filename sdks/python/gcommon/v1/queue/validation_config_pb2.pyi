from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationConfig(_message.Message):
    __slots__ = ("validate_schema", "max_body_bytes", "reject_invalid")
    VALIDATE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    MAX_BODY_BYTES_FIELD_NUMBER: _ClassVar[int]
    REJECT_INVALID_FIELD_NUMBER: _ClassVar[int]
    validate_schema: bool
    max_body_bytes: int
    reject_invalid: bool
    def __init__(self, validate_schema: _Optional[bool] = ..., max_body_bytes: _Optional[int] = ..., reject_invalid: _Optional[bool] = ...) -> None: ...
