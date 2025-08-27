import datetime

from gcommon.v1.common import alert_condition_pb2 as _alert_condition_pb2
from gcommon.v1.common import metrics_alert_severity_pb2 as _metrics_alert_severity_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertRule(_message.Message):
    __slots__ = (
        "name",
        "description",
        "metric_name",
        "condition",
        "threshold",
        "duration",
        "severity",
        "enabled",
        "labels",
    )
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    metric_name: str
    condition: _alert_condition_pb2.AlertCondition
    threshold: float
    duration: _duration_pb2.Duration
    severity: _metrics_alert_severity_pb2.MetricsAlertSeverity
    enabled: bool
    labels: _containers.ScalarMap[str, str]
    def __init__(
        self,
        name: _Optional[str] = ...,
        description: _Optional[str] = ...,
        metric_name: _Optional[str] = ...,
        condition: _Optional[_Union[_alert_condition_pb2.AlertCondition, str]] = ...,
        threshold: _Optional[float] = ...,
        duration: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        severity: _Optional[
            _Union[_metrics_alert_severity_pb2.MetricsAlertSeverity, str]
        ] = ...,
        enabled: _Optional[bool] = ...,
        labels: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
