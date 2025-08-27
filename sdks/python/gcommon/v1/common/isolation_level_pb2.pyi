from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationIsolationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISOLATION_LEVEL_UNSPECIFIED: _ClassVar[OrganizationIsolationLevel]
    ISOLATION_LEVEL_SHARED: _ClassVar[OrganizationIsolationLevel]
    ISOLATION_LEVEL_DATABASE: _ClassVar[OrganizationIsolationLevel]
    ISOLATION_LEVEL_INFRASTRUCTURE: _ClassVar[OrganizationIsolationLevel]
    ISOLATION_LEVEL_NETWORK: _ClassVar[OrganizationIsolationLevel]
    ISOLATION_LEVEL_PHYSICAL: _ClassVar[OrganizationIsolationLevel]

ISOLATION_LEVEL_UNSPECIFIED: OrganizationIsolationLevel
ISOLATION_LEVEL_SHARED: OrganizationIsolationLevel
ISOLATION_LEVEL_DATABASE: OrganizationIsolationLevel
ISOLATION_LEVEL_INFRASTRUCTURE: OrganizationIsolationLevel
ISOLATION_LEVEL_NETWORK: OrganizationIsolationLevel
ISOLATION_LEVEL_PHYSICAL: OrganizationIsolationLevel
