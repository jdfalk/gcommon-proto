import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JWTConfig(_message.Message):
    __slots__ = ("signing_algorithm", "access_token_ttl", "refresh_token_ttl")
    SIGNING_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    signing_algorithm: str
    access_token_ttl: _duration_pb2.Duration
    refresh_token_ttl: _duration_pb2.Duration
    def __init__(self, signing_algorithm: _Optional[str] = ..., access_token_ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., refresh_token_ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
