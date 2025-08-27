import datetime

from gcommon.v1.common import token_status_pb2 as _token_status_pb2
from gcommon.v1.common import token_type_pb2 as _token_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Token(_message.Message):
    __slots__ = ("id", "value", "type", "status", "user_id", "client_id", "scopes", "created_at", "expires_at", "last_used_at", "metadata", "ip_address", "user_agent", "refresh_token_id")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: str
    type: _token_type_pb2.TokenType
    status: _token_status_pb2.TokenStatus
    user_id: str
    client_id: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    last_used_at: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    ip_address: str
    user_agent: str
    refresh_token_id: str
    def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ..., type: _Optional[_Union[_token_type_pb2.TokenType, str]] = ..., status: _Optional[_Union[_token_status_pb2.TokenStatus, str]] = ..., user_id: _Optional[str] = ..., client_id: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_used_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., refresh_token_id: _Optional[str] = ...) -> None: ...
