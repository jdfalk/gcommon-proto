from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANNEL_TYPE_UNSPECIFIED: _ClassVar[ChannelType]
    CHANNEL_TYPE_EMAIL: _ClassVar[ChannelType]
    CHANNEL_TYPE_SLACK: _ClassVar[ChannelType]
    CHANNEL_TYPE_WEBHOOK: _ClassVar[ChannelType]
    CHANNEL_TYPE_SMS: _ClassVar[ChannelType]
    CHANNEL_TYPE_PAGERDUTY: _ClassVar[ChannelType]
    CHANNEL_TYPE_TEAMS: _ClassVar[ChannelType]
    CHANNEL_TYPE_DISCORD: _ClassVar[ChannelType]
    CHANNEL_TYPE_JIRA: _ClassVar[ChannelType]
CHANNEL_TYPE_UNSPECIFIED: ChannelType
CHANNEL_TYPE_EMAIL: ChannelType
CHANNEL_TYPE_SLACK: ChannelType
CHANNEL_TYPE_WEBHOOK: ChannelType
CHANNEL_TYPE_SMS: ChannelType
CHANNEL_TYPE_PAGERDUTY: ChannelType
CHANNEL_TYPE_TEAMS: ChannelType
CHANNEL_TYPE_DISCORD: ChannelType
CHANNEL_TYPE_JIRA: ChannelType
