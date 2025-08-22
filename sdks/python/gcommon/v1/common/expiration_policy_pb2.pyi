from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ExpirationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPIRATION_POLICY_UNSPECIFIED: _ClassVar[ExpirationPolicy]
    EXPIRATION_POLICY_TTL: _ClassVar[ExpirationPolicy]
    EXPIRATION_POLICY_IDLE: _ClassVar[ExpirationPolicy]
    EXPIRATION_POLICY_WRITE: _ClassVar[ExpirationPolicy]
    EXPIRATION_POLICY_NEVER: _ClassVar[ExpirationPolicy]
EXPIRATION_POLICY_UNSPECIFIED: ExpirationPolicy
EXPIRATION_POLICY_TTL: ExpirationPolicy
EXPIRATION_POLICY_IDLE: ExpirationPolicy
EXPIRATION_POLICY_WRITE: ExpirationPolicy
EXPIRATION_POLICY_NEVER: ExpirationPolicy
