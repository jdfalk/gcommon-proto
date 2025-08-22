from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CsrfConfig(_message.Message):
    __slots__ = ("header_name", "cookie_name", "token_length", "token_ttl", "secure")
    HEADER_NAME_FIELD_NUMBER: _ClassVar[int]
    COOKIE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    header_name: str
    cookie_name: str
    token_length: int
    token_ttl: _duration_pb2.Duration
    secure: bool
    def __init__(self, header_name: _Optional[str] = ..., cookie_name: _Optional[str] = ..., token_length: _Optional[int] = ..., token_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., secure: bool = ...) -> None: ...
