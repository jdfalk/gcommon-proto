from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MiddlewareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIDDLEWARE_TYPE_UNSPECIFIED: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_LOGGING: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_AUTHENTICATION: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_METRICS: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_COMPRESSION: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_CORS: _ClassVar[MiddlewareType]
    MIDDLEWARE_TYPE_RATE_LIMIT: _ClassVar[MiddlewareType]
MIDDLEWARE_TYPE_UNSPECIFIED: MiddlewareType
MIDDLEWARE_TYPE_LOGGING: MiddlewareType
MIDDLEWARE_TYPE_AUTHENTICATION: MiddlewareType
MIDDLEWARE_TYPE_METRICS: MiddlewareType
MIDDLEWARE_TYPE_COMPRESSION: MiddlewareType
MIDDLEWARE_TYPE_CORS: MiddlewareType
MIDDLEWARE_TYPE_RATE_LIMIT: MiddlewareType
