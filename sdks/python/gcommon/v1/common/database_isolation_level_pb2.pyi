from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseIsolationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATABASE_ISOLATION_LEVEL_UNSPECIFIED: _ClassVar[DatabaseIsolationLevel]
    DATABASE_ISOLATION_LEVEL_READ_UNCOMMITTED: _ClassVar[DatabaseIsolationLevel]
    DATABASE_ISOLATION_LEVEL_READ_COMMITTED: _ClassVar[DatabaseIsolationLevel]
    DATABASE_ISOLATION_LEVEL_REPEATABLE_READ: _ClassVar[DatabaseIsolationLevel]
    DATABASE_ISOLATION_LEVEL_SERIALIZABLE: _ClassVar[DatabaseIsolationLevel]

DATABASE_ISOLATION_LEVEL_UNSPECIFIED: DatabaseIsolationLevel
DATABASE_ISOLATION_LEVEL_READ_UNCOMMITTED: DatabaseIsolationLevel
DATABASE_ISOLATION_LEVEL_READ_COMMITTED: DatabaseIsolationLevel
DATABASE_ISOLATION_LEVEL_REPEATABLE_READ: DatabaseIsolationLevel
DATABASE_ISOLATION_LEVEL_SERIALIZABLE: DatabaseIsolationLevel
