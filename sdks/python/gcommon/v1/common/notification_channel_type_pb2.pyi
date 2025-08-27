from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_TYPE_EMAIL: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_TYPE_SLACK: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_TYPE_SMS: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_TYPE_WEBHOOK: _ClassVar[NotificationChannelType]
    NOTIFICATION_CHANNEL_TYPE_PAGERDUTY: _ClassVar[NotificationChannelType]

NOTIFICATION_CHANNEL_TYPE_UNSPECIFIED: NotificationChannelType
NOTIFICATION_CHANNEL_TYPE_EMAIL: NotificationChannelType
NOTIFICATION_CHANNEL_TYPE_SLACK: NotificationChannelType
NOTIFICATION_CHANNEL_TYPE_SMS: NotificationChannelType
NOTIFICATION_CHANNEL_TYPE_WEBHOOK: NotificationChannelType
NOTIFICATION_CHANNEL_TYPE_PAGERDUTY: NotificationChannelType
