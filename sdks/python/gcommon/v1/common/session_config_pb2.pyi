from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AuthSessionConfig(_message.Message):
    __slots__ = ("idle_timeout_seconds", "absolute_lifetime_seconds", "persist_across_restarts", "cookie_name", "secure_cookie")
    IDLE_TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_LIFETIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PERSIST_ACROSS_RESTARTS_FIELD_NUMBER: _ClassVar[int]
    COOKIE_NAME_FIELD_NUMBER: _ClassVar[int]
    SECURE_COOKIE_FIELD_NUMBER: _ClassVar[int]
    idle_timeout_seconds: int
    absolute_lifetime_seconds: int
    persist_across_restarts: bool
    cookie_name: str
    secure_cookie: bool
    def __init__(self, idle_timeout_seconds: _Optional[int] = ..., absolute_lifetime_seconds: _Optional[int] = ..., persist_across_restarts: bool = ..., cookie_name: _Optional[str] = ..., secure_cookie: bool = ...) -> None: ...
