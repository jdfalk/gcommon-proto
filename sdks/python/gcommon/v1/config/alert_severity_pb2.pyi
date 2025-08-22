from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigAlertSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_SEVERITY_UNSPECIFIED: _ClassVar[ConfigAlertSeverity]
    ALERT_SEVERITY_LOW: _ClassVar[ConfigAlertSeverity]
    ALERT_SEVERITY_MEDIUM: _ClassVar[ConfigAlertSeverity]
    ALERT_SEVERITY_HIGH: _ClassVar[ConfigAlertSeverity]
    ALERT_SEVERITY_CRITICAL: _ClassVar[ConfigAlertSeverity]
ALERT_SEVERITY_UNSPECIFIED: ConfigAlertSeverity
ALERT_SEVERITY_LOW: ConfigAlertSeverity
ALERT_SEVERITY_MEDIUM: ConfigAlertSeverity
ALERT_SEVERITY_HIGH: ConfigAlertSeverity
ALERT_SEVERITY_CRITICAL: ConfigAlertSeverity
