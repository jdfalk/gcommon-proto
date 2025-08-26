from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingSettings(_message.Message):
    __slots__ = ("routing_key_pattern", "target_partitions", "routing_strategy")
    ROUTING_KEY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    TARGET_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    routing_key_pattern: str
    target_partitions: _containers.RepeatedScalarFieldContainer[int]
    routing_strategy: str
    def __init__(self, routing_key_pattern: _Optional[str] = ..., target_partitions: _Optional[_Iterable[int]] = ..., routing_strategy: _Optional[str] = ...) -> None: ...
