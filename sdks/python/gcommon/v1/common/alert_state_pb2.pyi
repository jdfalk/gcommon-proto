from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlertState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_STATE_UNSPECIFIED: _ClassVar[AlertState]
    ALERT_STATE_PENDING: _ClassVar[AlertState]
    ALERT_STATE_FIRING: _ClassVar[AlertState]
    ALERT_STATE_RESOLVED: _ClassVar[AlertState]
    ALERT_STATE_ACKNOWLEDGED: _ClassVar[AlertState]
    ALERT_STATE_SILENCED: _ClassVar[AlertState]
    ALERT_STATE_ERROR: _ClassVar[AlertState]

ALERT_STATE_UNSPECIFIED: AlertState
ALERT_STATE_PENDING: AlertState
ALERT_STATE_FIRING: AlertState
ALERT_STATE_RESOLVED: AlertState
ALERT_STATE_ACKNOWLEDGED: AlertState
ALERT_STATE_SILENCED: AlertState
ALERT_STATE_ERROR: AlertState
