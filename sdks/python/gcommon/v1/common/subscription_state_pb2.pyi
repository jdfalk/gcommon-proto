from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_STATE_UNSPECIFIED: _ClassVar[SubscriptionState]
    SUBSCRIPTION_STATE_ACTIVE: _ClassVar[SubscriptionState]
    SUBSCRIPTION_STATE_PAUSED: _ClassVar[SubscriptionState]
    SUBSCRIPTION_STATE_CLOSED: _ClassVar[SubscriptionState]

SUBSCRIPTION_STATE_UNSPECIFIED: SubscriptionState
SUBSCRIPTION_STATE_ACTIVE: SubscriptionState
SUBSCRIPTION_STATE_PAUSED: SubscriptionState
SUBSCRIPTION_STATE_CLOSED: SubscriptionState
