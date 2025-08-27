from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_STRATEGY_UNSPECIFIED: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_DIRECT: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_TOPIC: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_FANOUT: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_HEADER: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_CONTENT: _ClassVar[RoutingStrategy]
    ROUTING_STRATEGY_HASH: _ClassVar[RoutingStrategy]

ROUTING_STRATEGY_UNSPECIFIED: RoutingStrategy
ROUTING_STRATEGY_DIRECT: RoutingStrategy
ROUTING_STRATEGY_TOPIC: RoutingStrategy
ROUTING_STRATEGY_FANOUT: RoutingStrategy
ROUTING_STRATEGY_HEADER: RoutingStrategy
ROUTING_STRATEGY_CONTENT: RoutingStrategy
ROUTING_STRATEGY_HASH: RoutingStrategy
