from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LoadBalancingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOAD_BALANCING_STRATEGY_UNSPECIFIED: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_ROUND_ROBIN: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_WEIGHTED_ROUND_ROBIN: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_LEAST_CONNECTIONS: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_RANDOM: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_HASH: _ClassVar[LoadBalancingStrategy]
    LOAD_BALANCING_STRATEGY_PRIORITY: _ClassVar[LoadBalancingStrategy]
LOAD_BALANCING_STRATEGY_UNSPECIFIED: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_ROUND_ROBIN: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_WEIGHTED_ROUND_ROBIN: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_LEAST_CONNECTIONS: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_RANDOM: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_HASH: LoadBalancingStrategy
LOAD_BALANCING_STRATEGY_PRIORITY: LoadBalancingStrategy
