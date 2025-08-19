from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LoadBalanceStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOAD_BALANCE_STRATEGY_UNSPECIFIED: _ClassVar[LoadBalanceStrategy]
    LOAD_BALANCE_STRATEGY_ROUND_ROBIN: _ClassVar[LoadBalanceStrategy]
    LOAD_BALANCE_STRATEGY_LEAST_CONNECTIONS: _ClassVar[LoadBalanceStrategy]
    LOAD_BALANCE_STRATEGY_IP_HASH: _ClassVar[LoadBalanceStrategy]
LOAD_BALANCE_STRATEGY_UNSPECIFIED: LoadBalanceStrategy
LOAD_BALANCE_STRATEGY_ROUND_ROBIN: LoadBalanceStrategy
LOAD_BALANCE_STRATEGY_LEAST_CONNECTIONS: LoadBalanceStrategy
LOAD_BALANCE_STRATEGY_IP_HASH: LoadBalanceStrategy
