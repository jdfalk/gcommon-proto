from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_SOURCE_UNSPECIFIED: _ClassVar[MetricSource]
    METRIC_SOURCE_APPLICATION: _ClassVar[MetricSource]
    METRIC_SOURCE_SYSTEM: _ClassVar[MetricSource]
    METRIC_SOURCE_INFRASTRUCTURE: _ClassVar[MetricSource]
    METRIC_SOURCE_CONTAINER: _ClassVar[MetricSource]
    METRIC_SOURCE_KUBERNETES: _ClassVar[MetricSource]
    METRIC_SOURCE_DATABASE: _ClassVar[MetricSource]
    METRIC_SOURCE_NETWORK: _ClassVar[MetricSource]
    METRIC_SOURCE_STORAGE: _ClassVar[MetricSource]
    METRIC_SOURCE_SECURITY: _ClassVar[MetricSource]
    METRIC_SOURCE_BUSINESS: _ClassVar[MetricSource]
    METRIC_SOURCE_CUSTOM: _ClassVar[MetricSource]
    METRIC_SOURCE_THIRD_PARTY: _ClassVar[MetricSource]
    METRIC_SOURCE_SYNTHETIC: _ClassVar[MetricSource]
    METRIC_SOURCE_LOG_DERIVED: _ClassVar[MetricSource]
METRIC_SOURCE_UNSPECIFIED: MetricSource
METRIC_SOURCE_APPLICATION: MetricSource
METRIC_SOURCE_SYSTEM: MetricSource
METRIC_SOURCE_INFRASTRUCTURE: MetricSource
METRIC_SOURCE_CONTAINER: MetricSource
METRIC_SOURCE_KUBERNETES: MetricSource
METRIC_SOURCE_DATABASE: MetricSource
METRIC_SOURCE_NETWORK: MetricSource
METRIC_SOURCE_STORAGE: MetricSource
METRIC_SOURCE_SECURITY: MetricSource
METRIC_SOURCE_BUSINESS: MetricSource
METRIC_SOURCE_CUSTOM: MetricSource
METRIC_SOURCE_THIRD_PARTY: MetricSource
METRIC_SOURCE_SYNTHETIC: MetricSource
METRIC_SOURCE_LOG_DERIVED: MetricSource
