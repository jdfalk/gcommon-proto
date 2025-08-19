from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_STATUS_UNSPECIFIED: _ClassVar[MetricStatus]
    METRIC_STATUS_ACTIVE: _ClassVar[MetricStatus]
    METRIC_STATUS_DISABLED: _ClassVar[MetricStatus]
    METRIC_STATUS_ERROR: _ClassVar[MetricStatus]
    METRIC_STATUS_DELETED: _ClassVar[MetricStatus]
METRIC_STATUS_UNSPECIFIED: MetricStatus
METRIC_STATUS_ACTIVE: MetricStatus
METRIC_STATUS_DISABLED: MetricStatus
METRIC_STATUS_ERROR: MetricStatus
METRIC_STATUS_DELETED: MetricStatus
