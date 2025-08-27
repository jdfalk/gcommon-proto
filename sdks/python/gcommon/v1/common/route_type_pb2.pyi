from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RouteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTE_TYPE_UNSPECIFIED: _ClassVar[RouteType]
    ROUTE_TYPE_STATIC_FILE: _ClassVar[RouteType]
    ROUTE_TYPE_API: _ClassVar[RouteType]
    ROUTE_TYPE_REDIRECT: _ClassVar[RouteType]
ROUTE_TYPE_UNSPECIFIED: RouteType
ROUTE_TYPE_STATIC_FILE: RouteType
ROUTE_TYPE_API: RouteType
ROUTE_TYPE_REDIRECT: RouteType
