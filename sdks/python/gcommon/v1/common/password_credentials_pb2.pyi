from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PasswordCredentials(_message.Message):
    __slots__ = ("username", "password", "remember_me")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_ME_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    remember_me: bool
    def __init__(
        self,
        username: _Optional[str] = ...,
        password: _Optional[str] = ...,
        remember_me: _Optional[bool] = ...,
    ) -> None: ...
