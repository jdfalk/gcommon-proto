from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsAlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SEVERITY_UNSPECIFIED: _ClassVar[MetricsAlertSeverity]
    ALERT_SEVERITY_LOW: _ClassVar[MetricsAlertSeverity]
    ALERT_SEVERITY_MEDIUM: _ClassVar[MetricsAlertSeverity]
    ALERT_SEVERITY_HIGH: _ClassVar[MetricsAlertSeverity]
    ALERT_SEVERITY_CRITICAL: _ClassVar[MetricsAlertSeverity]
ALERT_SEVERITY_UNSPECIFIED: MetricsAlertSeverity
ALERT_SEVERITY_LOW: MetricsAlertSeverity
ALERT_SEVERITY_MEDIUM: MetricsAlertSeverity
ALERT_SEVERITY_HIGH: MetricsAlertSeverity
ALERT_SEVERITY_CRITICAL: MetricsAlertSeverity
