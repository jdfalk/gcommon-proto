from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_STATUS_UNSPECIFIED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_ACTIVE: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_PAUSED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_CANCELLED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_ERROR: _ClassVar[SubscriptionStatus]
SUBSCRIPTION_STATUS_UNSPECIFIED: SubscriptionStatus
SUBSCRIPTION_STATUS_ACTIVE: SubscriptionStatus
SUBSCRIPTION_STATUS_PAUSED: SubscriptionStatus
SUBSCRIPTION_STATUS_CANCELLED: SubscriptionStatus
SUBSCRIPTION_STATUS_ERROR: SubscriptionStatus
