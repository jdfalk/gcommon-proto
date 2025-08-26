import datetime

from gcommon.v1.common import token_type_pb2 as _token_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenInfo(_message.Message):
    __slots__ = ("token_id", "type", "user_id", "client_id", "scopes", "created_at", "expires_at", "active", "expires_in")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    type: _token_type_pb2.TokenType
    user_id: str
    client_id: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    active: bool
    expires_in: int
    def __init__(self, token_id: _Optional[str] = ..., type: _Optional[_Union[_token_type_pb2.TokenType, str]] = ..., user_id: _Optional[str] = ..., client_id: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., active: _Optional[bool] = ..., expires_in: _Optional[int] = ...) -> None: ...
