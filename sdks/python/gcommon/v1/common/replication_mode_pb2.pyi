from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLICATION_MODE_UNSPECIFIED: _ClassVar[ReplicationMode]
    REPLICATION_MODE_NONE: _ClassVar[ReplicationMode]
    REPLICATION_MODE_SYNC: _ClassVar[ReplicationMode]
    REPLICATION_MODE_ASYNC: _ClassVar[ReplicationMode]
    REPLICATION_MODE_QUORUM: _ClassVar[ReplicationMode]
    REPLICATION_MODE_LEADER_FOLLOWER: _ClassVar[ReplicationMode]
    REPLICATION_MODE_MASTER_SLAVE: _ClassVar[ReplicationMode]
REPLICATION_MODE_UNSPECIFIED: ReplicationMode
REPLICATION_MODE_NONE: ReplicationMode
REPLICATION_MODE_SYNC: ReplicationMode
REPLICATION_MODE_ASYNC: ReplicationMode
REPLICATION_MODE_QUORUM: ReplicationMode
REPLICATION_MODE_LEADER_FOLLOWER: ReplicationMode
REPLICATION_MODE_MASTER_SLAVE: ReplicationMode
