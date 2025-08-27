from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DeliveryChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_CHANNEL_TYPE_UNSPECIFIED: _ClassVar[DeliveryChannelType]
    DELIVERY_CHANNEL_TYPE_EMAIL: _ClassVar[DeliveryChannelType]
    DELIVERY_CHANNEL_TYPE_SMS: _ClassVar[DeliveryChannelType]
    DELIVERY_CHANNEL_TYPE_SLACK: _ClassVar[DeliveryChannelType]
    DELIVERY_CHANNEL_TYPE_WEBHOOK: _ClassVar[DeliveryChannelType]

DELIVERY_CHANNEL_TYPE_UNSPECIFIED: DeliveryChannelType
DELIVERY_CHANNEL_TYPE_EMAIL: DeliveryChannelType
DELIVERY_CHANNEL_TYPE_SMS: DeliveryChannelType
DELIVERY_CHANNEL_TYPE_SLACK: DeliveryChannelType
DELIVERY_CHANNEL_TYPE_WEBHOOK: DeliveryChannelType
