from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_EMAIL: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SMS: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_PUSH: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SLACK: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_TEAMS: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_DISCORD: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_PAGERDUTY: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_WEBHOOK: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_IN_APP: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_SNMP: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_TELEGRAM: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_MATRIX: _ClassVar[NotificationType]
    NOTIFICATION_TYPE_VOICE: _ClassVar[NotificationType]
NOTIFICATION_TYPE_UNSPECIFIED: NotificationType
NOTIFICATION_TYPE_EMAIL: NotificationType
NOTIFICATION_TYPE_SMS: NotificationType
NOTIFICATION_TYPE_PUSH: NotificationType
NOTIFICATION_TYPE_SLACK: NotificationType
NOTIFICATION_TYPE_TEAMS: NotificationType
NOTIFICATION_TYPE_DISCORD: NotificationType
NOTIFICATION_TYPE_PAGERDUTY: NotificationType
NOTIFICATION_TYPE_WEBHOOK: NotificationType
NOTIFICATION_TYPE_IN_APP: NotificationType
NOTIFICATION_TYPE_SNMP: NotificationType
NOTIFICATION_TYPE_TELEGRAM: NotificationType
NOTIFICATION_TYPE_MATRIX: NotificationType
NOTIFICATION_TYPE_VOICE: NotificationType
