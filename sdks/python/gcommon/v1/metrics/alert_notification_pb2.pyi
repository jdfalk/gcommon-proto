from gcommon.v1.common import metrics_alert_severity_pb2 as _metrics_alert_severity_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertNotification(_message.Message):
    __slots__ = ("rule_id", "time", "severity", "message")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    time: _timestamp_pb2.Timestamp
    severity: _metrics_alert_severity_pb2.MetricsAlertSeverity
    message: str
    def __init__(self, rule_id: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., severity: _Optional[_Union[_metrics_alert_severity_pb2.MetricsAlertSeverity, str]] = ..., message: _Optional[str] = ...) -> None: ...
