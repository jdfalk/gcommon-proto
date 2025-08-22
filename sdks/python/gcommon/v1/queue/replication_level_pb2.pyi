from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLICATION_LEVEL_UNSPECIFIED: _ClassVar[ReplicationLevel]
    REPLICATION_LEVEL_ONE: _ClassVar[ReplicationLevel]
    REPLICATION_LEVEL_QUORUM: _ClassVar[ReplicationLevel]
    REPLICATION_LEVEL_ALL: _ClassVar[ReplicationLevel]
REPLICATION_LEVEL_UNSPECIFIED: ReplicationLevel
REPLICATION_LEVEL_ONE: ReplicationLevel
REPLICATION_LEVEL_QUORUM: ReplicationLevel
REPLICATION_LEVEL_ALL: ReplicationLevel
