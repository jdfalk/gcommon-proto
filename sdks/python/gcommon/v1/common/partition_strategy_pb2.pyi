from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTITION_STRATEGY_UNSPECIFIED: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_ROUND_ROBIN: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_HASH: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_RANDOM: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_MANUAL: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_STICKY: _ClassVar[PartitionStrategy]
    PARTITION_STRATEGY_LOAD_BALANCED: _ClassVar[PartitionStrategy]
PARTITION_STRATEGY_UNSPECIFIED: PartitionStrategy
PARTITION_STRATEGY_ROUND_ROBIN: PartitionStrategy
PARTITION_STRATEGY_HASH: PartitionStrategy
PARTITION_STRATEGY_RANDOM: PartitionStrategy
PARTITION_STRATEGY_MANUAL: PartitionStrategy
PARTITION_STRATEGY_STICKY: PartitionStrategy
PARTITION_STRATEGY_LOAD_BALANCED: PartitionStrategy
