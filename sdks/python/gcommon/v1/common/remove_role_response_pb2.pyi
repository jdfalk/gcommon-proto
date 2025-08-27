import datetime

from gcommon.v1.common import role_pb2 as _role_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveRoleResponse(_message.Message):
    __slots__ = (
        "user_id",
        "username",
        "role",
        "removed_at",
        "removed_by_user_id",
        "removed_by_username",
        "effective_immediately",
        "has_remaining_roles",
        "remaining_role_count",
        "message",
    )
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    REMOVED_AT_FIELD_NUMBER: _ClassVar[int]
    REMOVED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVED_BY_USERNAME_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    HAS_REMAINING_ROLES_FIELD_NUMBER: _ClassVar[int]
    REMAINING_ROLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    username: str
    role: _role_pb2.Role
    removed_at: _timestamp_pb2.Timestamp
    removed_by_user_id: str
    removed_by_username: str
    effective_immediately: bool
    has_remaining_roles: bool
    remaining_role_count: int
    message: str
    def __init__(
        self,
        user_id: _Optional[str] = ...,
        username: _Optional[str] = ...,
        role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...,
        removed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        removed_by_user_id: _Optional[str] = ...,
        removed_by_username: _Optional[str] = ...,
        effective_immediately: _Optional[bool] = ...,
        has_remaining_roles: _Optional[bool] = ...,
        remaining_role_count: _Optional[int] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...
