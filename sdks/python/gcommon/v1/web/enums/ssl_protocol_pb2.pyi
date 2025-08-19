from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SSLProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SSL_PROTOCOL_UNSPECIFIED: _ClassVar[SSLProtocol]
    SSL_PROTOCOL_TLS1_0: _ClassVar[SSLProtocol]
    SSL_PROTOCOL_TLS1_1: _ClassVar[SSLProtocol]
    SSL_PROTOCOL_TLS1_2: _ClassVar[SSLProtocol]
    SSL_PROTOCOL_TLS1_3: _ClassVar[SSLProtocol]
SSL_PROTOCOL_UNSPECIFIED: SSLProtocol
SSL_PROTOCOL_TLS1_0: SSLProtocol
SSL_PROTOCOL_TLS1_1: SSLProtocol
SSL_PROTOCOL_TLS1_2: SSLProtocol
SSL_PROTOCOL_TLS1_3: SSLProtocol
