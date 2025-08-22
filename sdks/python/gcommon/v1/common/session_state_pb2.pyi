from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMMON_SESSION_STATE_UNSPECIFIED: _ClassVar[SessionState]
    COMMON_SESSION_STATE_ACTIVE: _ClassVar[SessionState]
    COMMON_SESSION_STATE_EXPIRED: _ClassVar[SessionState]
COMMON_SESSION_STATE_UNSPECIFIED: SessionState
COMMON_SESSION_STATE_ACTIVE: SessionState
COMMON_SESSION_STATE_EXPIRED: SessionState
