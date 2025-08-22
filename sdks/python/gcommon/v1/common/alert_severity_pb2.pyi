from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CommonAlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SEVERITY_UNSPECIFIED: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_LOW: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_MEDIUM: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_HIGH: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_CRITICAL: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_INFO: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_WARNING: _ClassVar[CommonAlertSeverity]
    ALERT_SEVERITY_ERROR: _ClassVar[CommonAlertSeverity]
ALERT_SEVERITY_UNSPECIFIED: CommonAlertSeverity
ALERT_SEVERITY_LOW: CommonAlertSeverity
ALERT_SEVERITY_MEDIUM: CommonAlertSeverity
ALERT_SEVERITY_HIGH: CommonAlertSeverity
ALERT_SEVERITY_CRITICAL: CommonAlertSeverity
ALERT_SEVERITY_INFO: CommonAlertSeverity
ALERT_SEVERITY_WARNING: CommonAlertSeverity
ALERT_SEVERITY_ERROR: CommonAlertSeverity
