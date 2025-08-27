from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRICS_PROVIDER_TYPE_UNSPECIFIED: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_PROMETHEUS: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_INFLUXDB: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_GRAPHITE: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_DATADOG: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_NEW_RELIC: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_CLOUDWATCH: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_STACKDRIVER: _ClassVar[MetricsProviderType]
    METRICS_PROVIDER_TYPE_CUSTOM: _ClassVar[MetricsProviderType]

METRICS_PROVIDER_TYPE_UNSPECIFIED: MetricsProviderType
METRICS_PROVIDER_TYPE_PROMETHEUS: MetricsProviderType
METRICS_PROVIDER_TYPE_INFLUXDB: MetricsProviderType
METRICS_PROVIDER_TYPE_GRAPHITE: MetricsProviderType
METRICS_PROVIDER_TYPE_DATADOG: MetricsProviderType
METRICS_PROVIDER_TYPE_NEW_RELIC: MetricsProviderType
METRICS_PROVIDER_TYPE_CLOUDWATCH: MetricsProviderType
METRICS_PROVIDER_TYPE_STACKDRIVER: MetricsProviderType
METRICS_PROVIDER_TYPE_CUSTOM: MetricsProviderType
