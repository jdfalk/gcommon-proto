from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSystemStatsResponse(_message.Message):
    __slots__ = ("active_users", "total_roles", "active_sessions", "failed_logins", "uptime_seconds", "error")
    ACTIVE_USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROLES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    FAILED_LOGINS_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    active_users: int
    total_roles: int
    active_sessions: int
    failed_logins: int
    uptime_seconds: int
    error: _error_pb2.Error
    def __init__(self, active_users: _Optional[int] = ..., total_roles: _Optional[int] = ..., active_sessions: _Optional[int] = ..., failed_logins: _Optional[int] = ..., uptime_seconds: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
