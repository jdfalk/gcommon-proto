from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeApiKeyResponse(_message.Message):
    __slots__ = ("success", "error_message", "revoked_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    revoked_at: int
    def __init__(self, success: _Optional[bool] = ..., error_message: _Optional[str] = ..., revoked_at: _Optional[int] = ...) -> None: ...
