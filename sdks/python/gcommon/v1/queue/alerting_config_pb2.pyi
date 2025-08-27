import datetime

from gcommon.v1.common import alert_severity_pb2 as _alert_severity_pb2
from gcommon.v1.queue import alert_rule_pb2 as _alert_rule_pb2
from gcommon.v1.queue import notification_channel_pb2 as _notification_channel_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertingConfig(_message.Message):
    __slots__ = ("enabled", "rules", "channels", "default_severity", "aggregation_window")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_WINDOW_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    rules: _containers.RepeatedCompositeFieldContainer[_alert_rule_pb2.AlertRule]
    channels: _containers.RepeatedCompositeFieldContainer[_notification_channel_pb2.QueueNotificationChannel]
    default_severity: _alert_severity_pb2.CommonAlertSeverity
    aggregation_window: _duration_pb2.Duration
    def __init__(self, enabled: _Optional[bool] = ..., rules: _Optional[_Iterable[_Union[_alert_rule_pb2.AlertRule, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[_notification_channel_pb2.QueueNotificationChannel, _Mapping]]] = ..., default_severity: _Optional[_Union[_alert_severity_pb2.CommonAlertSeverity, str]] = ..., aggregation_window: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
