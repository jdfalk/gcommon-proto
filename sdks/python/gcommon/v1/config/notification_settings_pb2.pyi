from gcommon.v1.common import notification_trigger_pb2 as _notification_trigger_pb2
from gcommon.v1.config import batching_settings_pb2 as _batching_settings_pb2
from gcommon.v1.config import notification_channel_pb2 as _notification_channel_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigNotificationSettings(_message.Message):
    __slots__ = (
        "enabled",
        "channels",
        "triggers",
        "template",
        "recipients",
        "delay_minutes",
        "batching",
    )
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    DELAY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    BATCHING_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    channels: _containers.RepeatedCompositeFieldContainer[
        _notification_channel_pb2.ConfigNotificationChannel
    ]
    triggers: _containers.RepeatedScalarFieldContainer[
        _notification_trigger_pb2.NotificationTrigger
    ]
    template: str
    recipients: _containers.RepeatedScalarFieldContainer[str]
    delay_minutes: int
    batching: _batching_settings_pb2.BatchingSettings
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        channels: _Optional[
            _Iterable[
                _Union[_notification_channel_pb2.ConfigNotificationChannel, _Mapping]
            ]
        ] = ...,
        triggers: _Optional[
            _Iterable[_Union[_notification_trigger_pb2.NotificationTrigger, str]]
        ] = ...,
        template: _Optional[str] = ...,
        recipients: _Optional[_Iterable[str]] = ...,
        delay_minutes: _Optional[int] = ...,
        batching: _Optional[
            _Union[_batching_settings_pb2.BatchingSettings, _Mapping]
        ] = ...,
    ) -> None: ...
