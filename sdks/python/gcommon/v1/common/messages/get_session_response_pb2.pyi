from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.common.messages import session_pb2 as _session_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthGetSessionResponse(_message.Message):
    __slots__ = ("session", "error")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    session: _session_pb2.Session
    error: _error_pb2.Error
    def __init__(self, session: _Optional[_Union[_session_pb2.Session, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
