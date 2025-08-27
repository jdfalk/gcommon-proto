from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_TYPE_UNSPECIFIED: _ClassVar[AlertType]
    ALERT_TYPE_EXPIRATION: _ClassVar[AlertType]
    ALERT_TYPE_ACCESS_ANOMALY: _ClassVar[AlertType]
    ALERT_TYPE_FAILED_ACCESS: _ClassVar[AlertType]
    ALERT_TYPE_ROTATION_FAILURE: _ClassVar[AlertType]
    ALERT_TYPE_BACKUP_FAILURE: _ClassVar[AlertType]
    ALERT_TYPE_COMPLIANCE_VIOLATION: _ClassVar[AlertType]
    ALERT_TYPE_SECURITY_INCIDENT: _ClassVar[AlertType]

ALERT_TYPE_UNSPECIFIED: AlertType
ALERT_TYPE_EXPIRATION: AlertType
ALERT_TYPE_ACCESS_ANOMALY: AlertType
ALERT_TYPE_FAILED_ACCESS: AlertType
ALERT_TYPE_ROTATION_FAILURE: AlertType
ALERT_TYPE_BACKUP_FAILURE: AlertType
ALERT_TYPE_COMPLIANCE_VIOLATION: AlertType
ALERT_TYPE_SECURITY_INCIDENT: AlertType
