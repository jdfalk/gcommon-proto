from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseConsistencyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_CONSISTENCY_LEVEL_UNSPECIFIED: _ClassVar[DatabaseConsistencyLevel]
    DATABASE_CONSISTENCY_LEVEL_EVENTUAL: _ClassVar[DatabaseConsistencyLevel]
    DATABASE_CONSISTENCY_LEVEL_STRONG: _ClassVar[DatabaseConsistencyLevel]
    DATABASE_CONSISTENCY_LEVEL_BOUNDED_STALENESS: _ClassVar[DatabaseConsistencyLevel]

DATABASE_CONSISTENCY_LEVEL_UNSPECIFIED: DatabaseConsistencyLevel
DATABASE_CONSISTENCY_LEVEL_EVENTUAL: DatabaseConsistencyLevel
DATABASE_CONSISTENCY_LEVEL_STRONG: DatabaseConsistencyLevel
DATABASE_CONSISTENCY_LEVEL_BOUNDED_STALENESS: DatabaseConsistencyLevel
