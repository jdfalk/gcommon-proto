from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CacheKeyPolicy(_message.Message):
    __slots__ = ("include_query_strings", "query_string_whitelist", "include_headers", "header_whitelist", "include_cookies", "cookie_whitelist")
    INCLUDE_QUERY_STRINGS_FIELD_NUMBER: _ClassVar[int]
    QUERY_STRING_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    HEADER_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COOKIES_FIELD_NUMBER: _ClassVar[int]
    COOKIE_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    include_query_strings: bool
    query_string_whitelist: _containers.RepeatedScalarFieldContainer[str]
    include_headers: bool
    header_whitelist: _containers.RepeatedScalarFieldContainer[str]
    include_cookies: bool
    cookie_whitelist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_query_strings: bool = ..., query_string_whitelist: _Optional[_Iterable[str]] = ..., include_headers: bool = ..., header_whitelist: _Optional[_Iterable[str]] = ..., include_cookies: bool = ..., cookie_whitelist: _Optional[_Iterable[str]] = ...) -> None: ...
