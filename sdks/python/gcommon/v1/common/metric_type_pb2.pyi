from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsMetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_TYPE_UNSPECIFIED: _ClassVar[MetricsMetricType]
    METRIC_TYPE_COUNTER: _ClassVar[MetricsMetricType]
    METRIC_TYPE_GAUGE: _ClassVar[MetricsMetricType]
    METRIC_TYPE_HISTOGRAM: _ClassVar[MetricsMetricType]
    METRIC_TYPE_SUMMARY: _ClassVar[MetricsMetricType]
    METRIC_TYPE_TIMER: _ClassVar[MetricsMetricType]
    METRIC_TYPE_SET: _ClassVar[MetricsMetricType]

METRIC_TYPE_UNSPECIFIED: MetricsMetricType
METRIC_TYPE_COUNTER: MetricsMetricType
METRIC_TYPE_GAUGE: MetricsMetricType
METRIC_TYPE_HISTOGRAM: MetricsMetricType
METRIC_TYPE_SUMMARY: MetricsMetricType
METRIC_TYPE_TIMER: MetricsMetricType
METRIC_TYPE_SET: MetricsMetricType
