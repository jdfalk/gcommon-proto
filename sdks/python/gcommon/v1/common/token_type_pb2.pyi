from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_TYPE_UNSPECIFIED: _ClassVar[TokenType]
    TOKEN_TYPE_ACCESS: _ClassVar[TokenType]
    TOKEN_TYPE_REFRESH: _ClassVar[TokenType]
    TOKEN_TYPE_ID: _ClassVar[TokenType]
    TOKEN_TYPE_AUTHORIZATION_CODE: _ClassVar[TokenType]
    TOKEN_TYPE_API_KEY: _ClassVar[TokenType]
    TOKEN_TYPE_SESSION: _ClassVar[TokenType]
    TOKEN_TYPE_PASSWORD_RESET: _ClassVar[TokenType]
    TOKEN_TYPE_EMAIL_VERIFICATION: _ClassVar[TokenType]
    TOKEN_TYPE_PHONE_VERIFICATION: _ClassVar[TokenType]
    TOKEN_TYPE_INVITATION: _ClassVar[TokenType]

TOKEN_TYPE_UNSPECIFIED: TokenType
TOKEN_TYPE_ACCESS: TokenType
TOKEN_TYPE_REFRESH: TokenType
TOKEN_TYPE_ID: TokenType
TOKEN_TYPE_AUTHORIZATION_CODE: TokenType
TOKEN_TYPE_API_KEY: TokenType
TOKEN_TYPE_SESSION: TokenType
TOKEN_TYPE_PASSWORD_RESET: TokenType
TOKEN_TYPE_EMAIL_VERIFICATION: TokenType
TOKEN_TYPE_PHONE_VERIFICATION: TokenType
TOKEN_TYPE_INVITATION: TokenType
