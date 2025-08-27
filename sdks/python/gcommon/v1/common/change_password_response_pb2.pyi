from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangePasswordResponse(_message.Message):
    __slots__ = (
        "success",
        "message",
        "error",
        "sessions_terminated",
        "terminated_session_count",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_TERMINATED_FIELD_NUMBER: _ClassVar[int]
    TERMINATED_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    error: _error_pb2.Error
    sessions_terminated: bool
    terminated_session_count: int
    def __init__(
        self,
        success: _Optional[bool] = ...,
        message: _Optional[str] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        sessions_terminated: _Optional[bool] = ...,
        terminated_session_count: _Optional[int] = ...,
    ) -> None: ...
