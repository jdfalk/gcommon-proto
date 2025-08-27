from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendVerificationEmailResponse(_message.Message):
    __slots__ = ("sent", "error_message", "expires_at")
    SENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    sent: bool
    error_message: str
    expires_at: int
    def __init__(self, sent: _Optional[bool] = ..., error_message: _Optional[str] = ..., expires_at: _Optional[int] = ...) -> None: ...
