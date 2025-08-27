import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CORSConfig(_message.Message):
    __slots__ = ("enabled", "allowed_origins", "allowed_methods", "allowed_headers", "exposed_headers", "allow_credentials", "max_age")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_ORIGINS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_METHODS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_HEADERS_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    allowed_origins: _containers.RepeatedScalarFieldContainer[str]
    allowed_methods: _containers.RepeatedScalarFieldContainer[str]
    allowed_headers: _containers.RepeatedScalarFieldContainer[str]
    exposed_headers: _containers.RepeatedScalarFieldContainer[str]
    allow_credentials: bool
    max_age: _duration_pb2.Duration
    def __init__(self, enabled: _Optional[bool] = ..., allowed_origins: _Optional[_Iterable[str]] = ..., allowed_methods: _Optional[_Iterable[str]] = ..., allowed_headers: _Optional[_Iterable[str]] = ..., exposed_headers: _Optional[_Iterable[str]] = ..., allow_credentials: _Optional[bool] = ..., max_age: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
