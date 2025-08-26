from gcommon.v1.common import rate_limit_pb2 as _rate_limit_pb2
from gcommon.v1.common import session_pb2 as _session_pb2
from gcommon.v1.common import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAuthenticateResponse(_message.Message):
    __slots__ = ("access_token", "refresh_token", "token_type", "expires_in", "scopes", "user_info", "session", "rate_limit")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    scopes: _containers.RepeatedScalarFieldContainer[str]
    user_info: _user_info_pb2.UserInfo
    session: _session_pb2.Session
    rate_limit: _rate_limit_pb2.RateLimit
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., token_type: _Optional[str] = ..., expires_in: _Optional[int] = ..., scopes: _Optional[_Iterable[str]] = ..., user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ..., session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ..., rate_limit: _Optional[_Union[_rate_limit_pb2.RateLimit, _Mapping]] = ...) -> None: ...
