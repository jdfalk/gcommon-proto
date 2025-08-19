from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlertChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_CHANNEL_TYPE_UNSPECIFIED: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_EMAIL: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_SLACK: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_PAGERDUTY: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_WEBHOOK: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_SMS: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_TEAMS: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_DISCORD: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_TELEGRAM: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_PUSH: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_JIRA: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_SERVICENOW: _ClassVar[AlertChannelType]
    ALERT_CHANNEL_TYPE_CUSTOM: _ClassVar[AlertChannelType]
ALERT_CHANNEL_TYPE_UNSPECIFIED: AlertChannelType
ALERT_CHANNEL_TYPE_EMAIL: AlertChannelType
ALERT_CHANNEL_TYPE_SLACK: AlertChannelType
ALERT_CHANNEL_TYPE_PAGERDUTY: AlertChannelType
ALERT_CHANNEL_TYPE_WEBHOOK: AlertChannelType
ALERT_CHANNEL_TYPE_SMS: AlertChannelType
ALERT_CHANNEL_TYPE_TEAMS: AlertChannelType
ALERT_CHANNEL_TYPE_DISCORD: AlertChannelType
ALERT_CHANNEL_TYPE_TELEGRAM: AlertChannelType
ALERT_CHANNEL_TYPE_PUSH: AlertChannelType
ALERT_CHANNEL_TYPE_JIRA: AlertChannelType
ALERT_CHANNEL_TYPE_SERVICENOW: AlertChannelType
ALERT_CHANNEL_TYPE_CUSTOM: AlertChannelType
