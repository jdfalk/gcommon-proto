import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeTokenResponse(_message.Message):
    __slots__ = ("token_id", "token_type", "revoked_at", "user_id", "revocation_reason", "last_token_in_session")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_TOKEN_IN_SESSION_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    token_type: str
    revoked_at: _timestamp_pb2.Timestamp
    user_id: str
    revocation_reason: str
    last_token_in_session: bool
    def __init__(self, token_id: _Optional[str] = ..., token_type: _Optional[str] = ..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., revocation_reason: _Optional[str] = ..., last_token_in_session: _Optional[bool] = ...) -> None: ...
