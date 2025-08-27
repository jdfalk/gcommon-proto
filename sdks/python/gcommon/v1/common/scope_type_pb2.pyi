from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ScopeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCOPE_TYPE_UNSPECIFIED: _ClassVar[ScopeType]
    SCOPE_TYPE_GLOBAL: _ClassVar[ScopeType]
    SCOPE_TYPE_ORGANIZATION: _ClassVar[ScopeType]
    SCOPE_TYPE_PROJECT: _ClassVar[ScopeType]
    SCOPE_TYPE_RESOURCE: _ClassVar[ScopeType]

SCOPE_TYPE_UNSPECIFIED: ScopeType
SCOPE_TYPE_GLOBAL: ScopeType
SCOPE_TYPE_ORGANIZATION: ScopeType
SCOPE_TYPE_PROJECT: ScopeType
SCOPE_TYPE_RESOURCE: ScopeType
