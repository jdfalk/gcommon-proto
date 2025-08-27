from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SecretType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECRET_TYPE_UNSPECIFIED: _ClassVar[SecretType]
    SECRET_TYPE_PASSWORD: _ClassVar[SecretType]
    SECRET_TYPE_API_KEY: _ClassVar[SecretType]
    SECRET_TYPE_TOKEN: _ClassVar[SecretType]
    SECRET_TYPE_CERTIFICATE: _ClassVar[SecretType]
    SECRET_TYPE_PRIVATE_KEY: _ClassVar[SecretType]
    SECRET_TYPE_PUBLIC_KEY: _ClassVar[SecretType]
    SECRET_TYPE_OAUTH_CLIENT_SECRET: _ClassVar[SecretType]
    SECRET_TYPE_DATABASE_PASSWORD: _ClassVar[SecretType]
    SECRET_TYPE_CONNECTION_STRING: _ClassVar[SecretType]
    SECRET_TYPE_ENCRYPTION_KEY: _ClassVar[SecretType]
    SECRET_TYPE_SIGNING_KEY: _ClassVar[SecretType]
    SECRET_TYPE_SSH_KEY: _ClassVar[SecretType]
    SECRET_TYPE_TLS_CERTIFICATE: _ClassVar[SecretType]
    SECRET_TYPE_JWT_SECRET: _ClassVar[SecretType]
    SECRET_TYPE_WEBHOOK_SECRET: _ClassVar[SecretType]
    SECRET_TYPE_CUSTOM: _ClassVar[SecretType]

SECRET_TYPE_UNSPECIFIED: SecretType
SECRET_TYPE_PASSWORD: SecretType
SECRET_TYPE_API_KEY: SecretType
SECRET_TYPE_TOKEN: SecretType
SECRET_TYPE_CERTIFICATE: SecretType
SECRET_TYPE_PRIVATE_KEY: SecretType
SECRET_TYPE_PUBLIC_KEY: SecretType
SECRET_TYPE_OAUTH_CLIENT_SECRET: SecretType
SECRET_TYPE_DATABASE_PASSWORD: SecretType
SECRET_TYPE_CONNECTION_STRING: SecretType
SECRET_TYPE_ENCRYPTION_KEY: SecretType
SECRET_TYPE_SIGNING_KEY: SecretType
SECRET_TYPE_SSH_KEY: SecretType
SECRET_TYPE_TLS_CERTIFICATE: SecretType
SECRET_TYPE_JWT_SECRET: SecretType
SECRET_TYPE_WEBHOOK_SECRET: SecretType
SECRET_TYPE_CUSTOM: SecretType
