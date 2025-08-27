from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WebAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB_AUTH_METHOD_UNSPECIFIED: _ClassVar[WebAuthMethod]
    WEB_AUTH_METHOD_NONE: _ClassVar[WebAuthMethod]
    WEB_AUTH_METHOD_TOKEN: _ClassVar[WebAuthMethod]
    WEB_AUTH_METHOD_OAUTH2: _ClassVar[WebAuthMethod]

WEB_AUTH_METHOD_UNSPECIFIED: WebAuthMethod
WEB_AUTH_METHOD_NONE: WebAuthMethod
WEB_AUTH_METHOD_TOKEN: WebAuthMethod
WEB_AUTH_METHOD_OAUTH2: WebAuthMethod
