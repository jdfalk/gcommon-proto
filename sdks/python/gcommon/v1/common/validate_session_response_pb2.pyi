from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import session_pb2 as _session_pb2
from gcommon.v1.common import user_info_pb2 as _user_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateSessionResponse(_message.Message):
    __slots__ = ("valid", "session", "user_info", "error")
    VALID_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    session: _session_pb2.Session
    user_info: _user_info_pb2.UserInfo
    error: _error_pb2.Error
    def __init__(self, valid: bool = ..., session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ..., user_info: _Optional[_Union[_user_info_pb2.UserInfo, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
