from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyMfaResponse(_message.Message):
    __slots__ = ("verified", "error_message", "remaining_attempts", "session_token")
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMAINING_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    error_message: str
    remaining_attempts: int
    session_token: str
    def __init__(self, verified: _Optional[bool] = ..., error_message: _Optional[str] = ..., remaining_attempts: _Optional[int] = ..., session_token: _Optional[str] = ...) -> None: ...
