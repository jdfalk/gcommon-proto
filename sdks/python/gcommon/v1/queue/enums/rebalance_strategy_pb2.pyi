from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RebalanceStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REBALANCE_STRATEGY_UNSPECIFIED: _ClassVar[RebalanceStrategy]
    REBALANCE_STRATEGY_EAGER: _ClassVar[RebalanceStrategy]
    REBALANCE_STRATEGY_COOPERATIVE: _ClassVar[RebalanceStrategy]
    REBALANCE_STRATEGY_STATIC: _ClassVar[RebalanceStrategy]
REBALANCE_STRATEGY_UNSPECIFIED: RebalanceStrategy
REBALANCE_STRATEGY_EAGER: RebalanceStrategy
REBALANCE_STRATEGY_COOPERATIVE: RebalanceStrategy
REBALANCE_STRATEGY_STATIC: RebalanceStrategy
