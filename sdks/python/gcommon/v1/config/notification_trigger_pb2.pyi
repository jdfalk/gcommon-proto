from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_TRIGGER_UNSPECIFIED: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_CHANGE: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_DELETE: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_ERROR: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_APPROVAL: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_DEPLOYMENT: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_ROLLBACK: _ClassVar[NotificationTrigger]
    NOTIFICATION_TRIGGER_SCHEDULE: _ClassVar[NotificationTrigger]
NOTIFICATION_TRIGGER_UNSPECIFIED: NotificationTrigger
NOTIFICATION_TRIGGER_CHANGE: NotificationTrigger
NOTIFICATION_TRIGGER_DELETE: NotificationTrigger
NOTIFICATION_TRIGGER_ERROR: NotificationTrigger
NOTIFICATION_TRIGGER_APPROVAL: NotificationTrigger
NOTIFICATION_TRIGGER_DEPLOYMENT: NotificationTrigger
NOTIFICATION_TRIGGER_ROLLBACK: NotificationTrigger
NOTIFICATION_TRIGGER_SCHEDULE: NotificationTrigger
