from gcommon.v1.common import priority_level_pb2 as _priority_level_pb2
from gcommon.v1.common import routing_strategy_pb2 as _routing_strategy_pb2
from gcommon.v1.common import subscription_state_pb2 as _subscription_state_pb2
from gcommon.v1.queue import delivery_options_pb2 as _delivery_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionConfig(_message.Message):
    __slots__ = ("name", "state", "routing_strategy", "default_priority", "delivery_options", "max_inflight")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_INFLIGHT_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: _subscription_state_pb2.SubscriptionState
    routing_strategy: _routing_strategy_pb2.RoutingStrategy
    default_priority: _priority_level_pb2.PriorityLevel
    delivery_options: _delivery_options_pb2.DeliveryOptions
    max_inflight: int
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[_subscription_state_pb2.SubscriptionState, str]] = ..., routing_strategy: _Optional[_Union[_routing_strategy_pb2.RoutingStrategy, str]] = ..., default_priority: _Optional[_Union[_priority_level_pb2.PriorityLevel, str]] = ..., delivery_options: _Optional[_Union[_delivery_options_pb2.DeliveryOptions, _Mapping]] = ..., max_inflight: _Optional[int] = ...) -> None: ...
