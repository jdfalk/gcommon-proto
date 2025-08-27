import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAuthConfig(_message.Message):
    __slots__ = ("access_token_ttl", "refresh_token_ttl", "require_mfa")
    ACCESS_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_MFA_FIELD_NUMBER: _ClassVar[int]
    access_token_ttl: _timestamp_pb2.Timestamp
    refresh_token_ttl: _timestamp_pb2.Timestamp
    require_mfa: bool
    def __init__(self, access_token_ttl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., refresh_token_ttl: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., require_mfa: _Optional[bool] = ...) -> None: ...
