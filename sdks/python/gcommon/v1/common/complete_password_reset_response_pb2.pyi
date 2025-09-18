import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompletePasswordResetResponse(_message.Message):
    __slots__ = ("user_id", "username", "reset_completed_at", "sessions_terminated", "terminated_session_count", "tokens_revoked", "revoked_token_count", "requires_additional_verification", "message")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    RESET_COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_TERMINATED_FIELD_NUMBER: _ClassVar[int]
    TERMINATED_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_REVOKED_FIELD_NUMBER: _ClassVar[int]
    REVOKED_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_ADDITIONAL_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    username: str
    reset_completed_at: _timestamp_pb2.Timestamp
    sessions_terminated: bool
    terminated_session_count: int
    tokens_revoked: bool
    revoked_token_count: int
    requires_additional_verification: bool
    message: str
    def __init__(self, user_id: _Optional[str] = ..., username: _Optional[str] = ..., reset_completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sessions_terminated: _Optional[bool] = ..., terminated_session_count: _Optional[int] = ..., tokens_revoked: _Optional[bool] = ..., revoked_token_count: _Optional[int] = ..., requires_additional_verification: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
