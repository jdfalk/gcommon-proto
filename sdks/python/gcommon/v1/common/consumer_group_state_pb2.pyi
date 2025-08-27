from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerGroupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSUMER_GROUP_STATE_UNSPECIFIED: _ClassVar[ConsumerGroupState]
    CONSUMER_GROUP_STATE_STABLE: _ClassVar[ConsumerGroupState]
    CONSUMER_GROUP_STATE_PREPARING_REBALANCE: _ClassVar[ConsumerGroupState]
    CONSUMER_GROUP_STATE_COMPLETING_REBALANCE: _ClassVar[ConsumerGroupState]
    CONSUMER_GROUP_STATE_DEAD: _ClassVar[ConsumerGroupState]
    CONSUMER_GROUP_STATE_EMPTY: _ClassVar[ConsumerGroupState]
CONSUMER_GROUP_STATE_UNSPECIFIED: ConsumerGroupState
CONSUMER_GROUP_STATE_STABLE: ConsumerGroupState
CONSUMER_GROUP_STATE_PREPARING_REBALANCE: ConsumerGroupState
CONSUMER_GROUP_STATE_COMPLETING_REBALANCE: ConsumerGroupState
CONSUMER_GROUP_STATE_DEAD: ConsumerGroupState
CONSUMER_GROUP_STATE_EMPTY: ConsumerGroupState
