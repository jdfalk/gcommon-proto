from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WebSessionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_SESSION_STATE_UNSPECIFIED: _ClassVar[WebSessionState]
    WEB_SESSION_STATE_ACTIVE: _ClassVar[WebSessionState]
    WEB_SESSION_STATE_EXPIRED: _ClassVar[WebSessionState]
    WEB_SESSION_STATE_REVOKED: _ClassVar[WebSessionState]

WEB_SESSION_STATE_UNSPECIFIED: WebSessionState
WEB_SESSION_STATE_ACTIVE: WebSessionState
WEB_SESSION_STATE_EXPIRED: WebSessionState
WEB_SESSION_STATE_REVOKED: WebSessionState
