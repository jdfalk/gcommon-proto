from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyEmailResponse(_message.Message):
    __slots__ = ("verified", "error_message", "user_id")
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    verified: bool
    error_message: str
    user_id: str
    def __init__(
        self,
        verified: _Optional[bool] = ...,
        error_message: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
    ) -> None: ...
