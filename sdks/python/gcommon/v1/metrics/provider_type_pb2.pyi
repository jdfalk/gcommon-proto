from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_TYPE_UNSPECIFIED: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_PROMETHEUS: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_OPENTELEMETRY: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_STATSD: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_CUSTOM: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_MEMORY: _ClassVar[MetricsProviderType]
    PROVIDER_TYPE_MULTI: _ClassVar[MetricsProviderType]
PROVIDER_TYPE_UNSPECIFIED: MetricsProviderType
PROVIDER_TYPE_PROMETHEUS: MetricsProviderType
PROVIDER_TYPE_OPENTELEMETRY: MetricsProviderType
PROVIDER_TYPE_STATSD: MetricsProviderType
PROVIDER_TYPE_CUSTOM: MetricsProviderType
PROVIDER_TYPE_MEMORY: MetricsProviderType
PROVIDER_TYPE_MULTI: MetricsProviderType
