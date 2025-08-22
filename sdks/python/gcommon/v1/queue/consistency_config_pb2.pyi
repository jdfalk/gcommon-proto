from gcommon.v1.config import conflict_resolution_pb2 as _conflict_resolution_pb2
from gcommon.v1.queue import ack_level_pb2 as _ack_level_pb2
from gcommon.v1.queue import durability_level_pb2 as _durability_level_pb2
from gcommon.v1.queue import consistency_validation_pb2 as _consistency_validation_pb2
from gcommon.v1.queue import ordering_config_pb2 as _ordering_config_pb2
from gcommon.v1.queue import read_consistency_pb2 as _read_consistency_pb2
from gcommon.v1.queue import replication_consistency_pb2 as _replication_consistency_pb2
from gcommon.v1.queue import write_consistency_pb2 as _write_consistency_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsistencyConfig(_message.Message):
    __slots__ = ("durability_level", "ack_level", "replication", "read_consistency", "write_consistency", "ordering", "conflict_resolution", "validation")
    DURABILITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FIELD_NUMBER: _ClassVar[int]
    READ_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    WRITE_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    ORDERING_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    durability_level: _durability_level_pb2.DurabilityLevel
    ack_level: _ack_level_pb2.AckLevel
    replication: _replication_consistency_pb2.ReplicationConsistency
    read_consistency: _read_consistency_pb2.ReadConsistency
    write_consistency: _write_consistency_pb2.WriteConsistency
    ordering: _ordering_config_pb2.OrderingConfig
    conflict_resolution: _conflict_resolution_pb2.ConfigConflictResolution
    validation: _consistency_validation_pb2.ConsistencyValidation
    def __init__(self, durability_level: _Optional[_Union[_durability_level_pb2.DurabilityLevel, str]] = ..., ack_level: _Optional[_Union[_ack_level_pb2.AckLevel, str]] = ..., replication: _Optional[_Union[_replication_consistency_pb2.ReplicationConsistency, _Mapping]] = ..., read_consistency: _Optional[_Union[_read_consistency_pb2.ReadConsistency, _Mapping]] = ..., write_consistency: _Optional[_Union[_write_consistency_pb2.WriteConsistency, _Mapping]] = ..., ordering: _Optional[_Union[_ordering_config_pb2.OrderingConfig, _Mapping]] = ..., conflict_resolution: _Optional[_Union[_conflict_resolution_pb2.ConfigConflictResolution, str]] = ..., validation: _Optional[_Union[_consistency_validation_pb2.ConsistencyValidation, _Mapping]] = ...) -> None: ...
