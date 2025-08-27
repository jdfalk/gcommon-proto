from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IntegrityValidation(_message.Message):
    __slots__ = ("passed", "corrupted_messages", "missing_messages", "duplicate_messages")
    PASSED_FIELD_NUMBER: _ClassVar[int]
    CORRUPTED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MISSING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    passed: bool
    corrupted_messages: int
    missing_messages: int
    duplicate_messages: int
    def __init__(self, passed: _Optional[bool] = ..., corrupted_messages: _Optional[int] = ..., missing_messages: _Optional[int] = ..., duplicate_messages: _Optional[int] = ...) -> None: ...
