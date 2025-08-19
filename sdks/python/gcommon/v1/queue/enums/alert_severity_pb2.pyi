from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueAlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SEVERITY_UNSPECIFIED: _ClassVar[QueueAlertSeverity]
    ALERT_SEVERITY_INFO: _ClassVar[QueueAlertSeverity]
    ALERT_SEVERITY_WARNING: _ClassVar[QueueAlertSeverity]
    ALERT_SEVERITY_ERROR: _ClassVar[QueueAlertSeverity]
    ALERT_SEVERITY_CRITICAL: _ClassVar[QueueAlertSeverity]
ALERT_SEVERITY_UNSPECIFIED: QueueAlertSeverity
ALERT_SEVERITY_INFO: QueueAlertSeverity
ALERT_SEVERITY_WARNING: QueueAlertSeverity
ALERT_SEVERITY_ERROR: QueueAlertSeverity
ALERT_SEVERITY_CRITICAL: QueueAlertSeverity
