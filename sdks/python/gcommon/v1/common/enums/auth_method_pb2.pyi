from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUTH_METHOD_UNSPECIFIED: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_PASSWORD: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_API_KEY: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_OAUTH2: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_SAML: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_LDAP: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_MFA: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_TOKEN: _ClassVar[AuthAuthMethod]
    AUTH_METHOD_NONE: _ClassVar[AuthAuthMethod]
AUTH_METHOD_UNSPECIFIED: AuthAuthMethod
AUTH_METHOD_PASSWORD: AuthAuthMethod
AUTH_METHOD_API_KEY: AuthAuthMethod
AUTH_METHOD_OAUTH2: AuthAuthMethod
AUTH_METHOD_SAML: AuthAuthMethod
AUTH_METHOD_LDAP: AuthAuthMethod
AUTH_METHOD_MFA: AuthAuthMethod
AUTH_METHOD_TOKEN: AuthAuthMethod
AUTH_METHOD_NONE: AuthAuthMethod
