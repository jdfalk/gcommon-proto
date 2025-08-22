from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthSessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_STATE_UNSPECIFIED: _ClassVar[AuthSessionState]
    SESSION_STATE_ACTIVE: _ClassVar[AuthSessionState]
    SESSION_STATE_IDLE: _ClassVar[AuthSessionState]
    SESSION_STATE_EXPIRED: _ClassVar[AuthSessionState]
    SESSION_STATE_TERMINATED: _ClassVar[AuthSessionState]
SESSION_STATE_UNSPECIFIED: AuthSessionState
SESSION_STATE_ACTIVE: AuthSessionState
SESSION_STATE_IDLE: AuthSessionState
SESSION_STATE_EXPIRED: AuthSessionState
SESSION_STATE_TERMINATED: AuthSessionState
