from gcommon.v1.common import metrics_alert_severity_pb2 as _metrics_alert_severity_pb2
from gcommon.v1.common import notification_channel_type_pb2 as _notification_channel_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueNotificationChannel(_message.Message):
    __slots__ = ("id", "type", "config", "enabled", "min_severity")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_SEVERITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _notification_channel_type_pb2.NotificationChannelType
    config: _containers.ScalarMap[str, str]
    enabled: bool
    min_severity: _metrics_alert_severity_pb2.MetricsAlertSeverity
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_notification_channel_type_pb2.NotificationChannelType, str]] = ..., config: _Optional[_Mapping[str, str]] = ..., enabled: _Optional[bool] = ..., min_severity: _Optional[_Union[_metrics_alert_severity_pb2.MetricsAlertSeverity, str]] = ...) -> None: ...
