from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TokenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_STATUS_UNSPECIFIED: _ClassVar[TokenStatus]
    TOKEN_STATUS_ACTIVE: _ClassVar[TokenStatus]
    TOKEN_STATUS_EXPIRED: _ClassVar[TokenStatus]
    TOKEN_STATUS_REVOKED: _ClassVar[TokenStatus]
    TOKEN_STATUS_SUSPENDED: _ClassVar[TokenStatus]
    TOKEN_STATUS_PENDING: _ClassVar[TokenStatus]
    TOKEN_STATUS_INVALID: _ClassVar[TokenStatus]
TOKEN_STATUS_UNSPECIFIED: TokenStatus
TOKEN_STATUS_ACTIVE: TokenStatus
TOKEN_STATUS_EXPIRED: TokenStatus
TOKEN_STATUS_REVOKED: TokenStatus
TOKEN_STATUS_SUSPENDED: TokenStatus
TOKEN_STATUS_PENDING: TokenStatus
TOKEN_STATUS_INVALID: TokenStatus
