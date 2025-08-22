from gcommon.v1.web import cookie_same_site_pb2 as _cookie_same_site_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CookieData(_message.Message):
    __slots__ = ("name", "value", "path", "domain", "expires_at", "http_only", "secure", "same_site")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    HTTP_ONLY_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    SAME_SITE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    path: str
    domain: str
    expires_at: _timestamp_pb2.Timestamp
    http_only: bool
    secure: bool
    same_site: _cookie_same_site_pb2.CookieSameSite
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., path: _Optional[str] = ..., domain: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., http_only: bool = ..., secure: bool = ..., same_site: _Optional[_Union[_cookie_same_site_pb2.CookieSameSite, str]] = ...) -> None: ...
