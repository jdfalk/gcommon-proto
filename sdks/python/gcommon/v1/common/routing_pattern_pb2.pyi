from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingPattern(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROUTING_PATTERN_UNSPECIFIED: _ClassVar[RoutingPattern]
    ROUTING_PATTERN_WILDCARD: _ClassVar[RoutingPattern]
    ROUTING_PATTERN_REGEX: _ClassVar[RoutingPattern]
    ROUTING_PATTERN_TOPIC: _ClassVar[RoutingPattern]
    ROUTING_PATTERN_PREFIX: _ClassVar[RoutingPattern]
    ROUTING_PATTERN_SUFFIX: _ClassVar[RoutingPattern]

ROUTING_PATTERN_UNSPECIFIED: RoutingPattern
ROUTING_PATTERN_WILDCARD: RoutingPattern
ROUTING_PATTERN_REGEX: RoutingPattern
ROUTING_PATTERN_TOPIC: RoutingPattern
ROUTING_PATTERN_PREFIX: RoutingPattern
ROUTING_PATTERN_SUFFIX: RoutingPattern
