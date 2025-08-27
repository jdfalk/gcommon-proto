from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HandlerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HANDLER_TYPE_UNSPECIFIED: _ClassVar[HandlerType]
    HANDLER_TYPE_HTTP: _ClassVar[HandlerType]
    HANDLER_TYPE_GRPC: _ClassVar[HandlerType]
    HANDLER_TYPE_WEBSOCKET: _ClassVar[HandlerType]

HANDLER_TYPE_UNSPECIFIED: HandlerType
HANDLER_TYPE_HTTP: HandlerType
HANDLER_TYPE_GRPC: HandlerType
HANDLER_TYPE_WEBSOCKET: HandlerType
