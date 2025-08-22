from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AlertCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALERT_CONDITION_UNSPECIFIED: _ClassVar[AlertCondition]
    ALERT_CONDITION_GREATER_THAN: _ClassVar[AlertCondition]
    ALERT_CONDITION_LESS_THAN: _ClassVar[AlertCondition]
    ALERT_CONDITION_EQUALS: _ClassVar[AlertCondition]
    ALERT_CONDITION_NOT_EQUALS: _ClassVar[AlertCondition]
    ALERT_CONDITION_INCREASING: _ClassVar[AlertCondition]
    ALERT_CONDITION_DECREASING: _ClassVar[AlertCondition]
ALERT_CONDITION_UNSPECIFIED: AlertCondition
ALERT_CONDITION_GREATER_THAN: AlertCondition
ALERT_CONDITION_LESS_THAN: AlertCondition
ALERT_CONDITION_EQUALS: AlertCondition
ALERT_CONDITION_NOT_EQUALS: AlertCondition
ALERT_CONDITION_INCREASING: AlertCondition
ALERT_CONDITION_DECREASING: AlertCondition
