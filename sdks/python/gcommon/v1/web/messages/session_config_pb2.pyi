from gcommon.v1.web.enums import cookie_same_site_pb2 as _cookie_same_site_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebSessionConfig(_message.Message):
    __slots__ = ("idle_timeout", "absolute_timeout", "cookie_name", "secure_cookies", "http_only", "same_site")
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    COOKIE_NAME_FIELD_NUMBER: _ClassVar[int]
    SECURE_COOKIES_FIELD_NUMBER: _ClassVar[int]
    HTTP_ONLY_FIELD_NUMBER: _ClassVar[int]
    SAME_SITE_FIELD_NUMBER: _ClassVar[int]
    idle_timeout: _duration_pb2.Duration
    absolute_timeout: _duration_pb2.Duration
    cookie_name: str
    secure_cookies: bool
    http_only: bool
    same_site: _cookie_same_site_pb2.CookieSameSite
    def __init__(self, idle_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., absolute_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cookie_name: _Optional[str] = ..., secure_cookies: bool = ..., http_only: bool = ..., same_site: _Optional[_Union[_cookie_same_site_pb2.CookieSameSite, str]] = ...) -> None: ...
