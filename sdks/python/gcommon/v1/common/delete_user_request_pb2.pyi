from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteUserRequest(_message.Message):
    __slots__ = ("user_id", "soft_delete", "reason", "transfer_to_user_id", "revoke_sessions")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SOFT_DELETE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TO_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    soft_delete: bool
    reason: str
    transfer_to_user_id: str
    revoke_sessions: bool
    def __init__(self, user_id: _Optional[str] = ..., soft_delete: _Optional[bool] = ..., reason: _Optional[str] = ..., transfer_to_user_id: _Optional[str] = ..., revoke_sessions: _Optional[bool] = ...) -> None: ...
