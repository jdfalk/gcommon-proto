from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AuthProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TYPE_UNSPECIFIED: _ClassVar[AuthProviderType]
    PROVIDER_TYPE_LOCAL: _ClassVar[AuthProviderType]
    PROVIDER_TYPE_LDAP: _ClassVar[AuthProviderType]
    PROVIDER_TYPE_SAML: _ClassVar[AuthProviderType]
    PROVIDER_TYPE_OAUTH2: _ClassVar[AuthProviderType]
PROVIDER_TYPE_UNSPECIFIED: AuthProviderType
PROVIDER_TYPE_LOCAL: AuthProviderType
PROVIDER_TYPE_LDAP: AuthProviderType
PROVIDER_TYPE_SAML: AuthProviderType
PROVIDER_TYPE_OAUTH2: AuthProviderType
