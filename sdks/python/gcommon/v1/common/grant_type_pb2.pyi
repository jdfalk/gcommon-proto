from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRANT_TYPE_UNSPECIFIED: _ClassVar[GrantType]
    GRANT_TYPE_AUTHORIZATION_CODE: _ClassVar[GrantType]
    GRANT_TYPE_IMPLICIT: _ClassVar[GrantType]
    GRANT_TYPE_PASSWORD: _ClassVar[GrantType]
    GRANT_TYPE_CLIENT_CREDENTIALS: _ClassVar[GrantType]
    GRANT_TYPE_REFRESH_TOKEN: _ClassVar[GrantType]
    GRANT_TYPE_DEVICE_CODE: _ClassVar[GrantType]
    GRANT_TYPE_SAML2_BEARER: _ClassVar[GrantType]
GRANT_TYPE_UNSPECIFIED: GrantType
GRANT_TYPE_AUTHORIZATION_CODE: GrantType
GRANT_TYPE_IMPLICIT: GrantType
GRANT_TYPE_PASSWORD: GrantType
GRANT_TYPE_CLIENT_CREDENTIALS: GrantType
GRANT_TYPE_REFRESH_TOKEN: GrantType
GRANT_TYPE_DEVICE_CODE: GrantType
GRANT_TYPE_SAML2_BEARER: GrantType
