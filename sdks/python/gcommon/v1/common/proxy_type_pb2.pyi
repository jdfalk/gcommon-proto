from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ProxyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROXY_TYPE_UNSPECIFIED: _ClassVar[ProxyType]
    PROXY_TYPE_FORWARD: _ClassVar[ProxyType]
    PROXY_TYPE_REVERSE: _ClassVar[ProxyType]
    PROXY_TYPE_TRANSPARENT: _ClassVar[ProxyType]
PROXY_TYPE_UNSPECIFIED: ProxyType
PROXY_TYPE_FORWARD: ProxyType
PROXY_TYPE_REVERSE: ProxyType
PROXY_TYPE_TRANSPARENT: ProxyType
