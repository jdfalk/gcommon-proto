from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseIsolationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISOLATION_LEVEL_UNSPECIFIED: _ClassVar[DatabaseIsolationLevel]
    ISOLATION_LEVEL_READ_UNCOMMITTED: _ClassVar[DatabaseIsolationLevel]
    ISOLATION_LEVEL_READ_COMMITTED: _ClassVar[DatabaseIsolationLevel]
    ISOLATION_LEVEL_REPEATABLE_READ: _ClassVar[DatabaseIsolationLevel]
    ISOLATION_LEVEL_SERIALIZABLE: _ClassVar[DatabaseIsolationLevel]
ISOLATION_LEVEL_UNSPECIFIED: DatabaseIsolationLevel
ISOLATION_LEVEL_READ_UNCOMMITTED: DatabaseIsolationLevel
ISOLATION_LEVEL_READ_COMMITTED: DatabaseIsolationLevel
ISOLATION_LEVEL_REPEATABLE_READ: DatabaseIsolationLevel
ISOLATION_LEVEL_SERIALIZABLE: DatabaseIsolationLevel
