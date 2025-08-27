from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SessionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SESSION_STATUS_UNSPECIFIED: _ClassVar[SessionStatus]
    SESSION_STATUS_ACTIVE: _ClassVar[SessionStatus]
    SESSION_STATUS_EXPIRED: _ClassVar[SessionStatus]
    SESSION_STATUS_TERMINATED: _ClassVar[SessionStatus]
    SESSION_STATUS_INVALID: _ClassVar[SessionStatus]
SESSION_STATUS_UNSPECIFIED: SessionStatus
SESSION_STATUS_ACTIVE: SessionStatus
SESSION_STATUS_EXPIRED: SessionStatus
SESSION_STATUS_TERMINATED: SessionStatus
SESSION_STATUS_INVALID: SessionStatus
