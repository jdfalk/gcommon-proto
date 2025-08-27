from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WebSocketState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_SOCKET_STATE_UNSPECIFIED: _ClassVar[WebSocketState]
    WEB_SOCKET_STATE_CONNECTING: _ClassVar[WebSocketState]
    WEB_SOCKET_STATE_OPEN: _ClassVar[WebSocketState]
    WEB_SOCKET_STATE_CLOSING: _ClassVar[WebSocketState]
    WEB_SOCKET_STATE_CLOSED: _ClassVar[WebSocketState]

WEB_SOCKET_STATE_UNSPECIFIED: WebSocketState
WEB_SOCKET_STATE_CONNECTING: WebSocketState
WEB_SOCKET_STATE_OPEN: WebSocketState
WEB_SOCKET_STATE_CLOSING: WebSocketState
WEB_SOCKET_STATE_CLOSED: WebSocketState
