from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterUserResponse(_message.Message):
    __slots__ = ("success", "user_id", "email_verification_required", "error_message", "session_token")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFICATION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    success: bool
    user_id: str
    email_verification_required: bool
    error_message: str
    session_token: str
    def __init__(self, success: _Optional[bool] = ..., user_id: _Optional[str] = ..., email_verification_required: _Optional[bool] = ..., error_message: _Optional[str] = ..., session_token: _Optional[str] = ...) -> None: ...
