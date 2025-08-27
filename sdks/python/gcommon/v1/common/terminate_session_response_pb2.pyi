import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TerminateSessionResponse(_message.Message):
    __slots__ = ("session_id", "user_id", "username", "terminated_at", "termination_reason", "tokens_revoked", "revoked_token_count", "forced_termination", "remaining_session_count", "message")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TERMINATED_AT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REASON_FIELD_NUMBER: _ClassVar[int]
    TOKENS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    FORCED_TERMINATION_FIELD_NUMBER: _ClassVar[int]
    REMAINING_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    username: str
    terminated_at: _timestamp_pb2.Timestamp
    termination_reason: str
    tokens_revoked: bool
    revoked_token_count: int
    forced_termination: bool
    remaining_session_count: int
    message: str
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ..., username: _Optional[str] = ..., terminated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., termination_reason: _Optional[str] = ..., tokens_revoked: _Optional[bool] = ..., revoked_token_count: _Optional[int] = ..., forced_termination: _Optional[bool] = ..., remaining_session_count: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
