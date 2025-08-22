from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WebAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_METHOD_UNSPECIFIED: _ClassVar[WebAuthMethod]
    AUTH_METHOD_NONE: _ClassVar[WebAuthMethod]
    AUTH_METHOD_BASIC: _ClassVar[WebAuthMethod]
    AUTH_METHOD_TOKEN: _ClassVar[WebAuthMethod]
    AUTH_METHOD_OAUTH2: _ClassVar[WebAuthMethod]
AUTH_METHOD_UNSPECIFIED: WebAuthMethod
AUTH_METHOD_NONE: WebAuthMethod
AUTH_METHOD_BASIC: WebAuthMethod
AUTH_METHOD_TOKEN: WebAuthMethod
AUTH_METHOD_OAUTH2: WebAuthMethod
