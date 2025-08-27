import datetime

from gcommon.v1.common import cookie_same_site_pb2 as _cookie_same_site_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CookieConfig(_message.Message):
    __slots__ = ("name", "domain", "path", "secure", "http_only", "same_site", "max_age")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    HTTP_ONLY_FIELD_NUMBER: _ClassVar[int]
    SAME_SITE_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    path: str
    secure: bool
    http_only: bool
    same_site: _cookie_same_site_pb2.CookieSameSite
    max_age: _duration_pb2.Duration
    def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., path: _Optional[str] = ..., secure: _Optional[bool] = ..., http_only: _Optional[bool] = ..., same_site: _Optional[_Union[_cookie_same_site_pb2.CookieSameSite, str]] = ..., max_age: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
