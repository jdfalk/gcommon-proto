from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRICS_EXPORT_FORMAT_UNSPECIFIED: _ClassVar[MetricsExportFormat]
    METRICS_EXPORT_FORMAT_PROMETHEUS: _ClassVar[MetricsExportFormat]
    METRICS_EXPORT_FORMAT_JSON: _ClassVar[MetricsExportFormat]
    METRICS_EXPORT_FORMAT_CSV: _ClassVar[MetricsExportFormat]
    METRICS_EXPORT_FORMAT_OPENTELEMETRY: _ClassVar[MetricsExportFormat]

METRICS_EXPORT_FORMAT_UNSPECIFIED: MetricsExportFormat
METRICS_EXPORT_FORMAT_PROMETHEUS: MetricsExportFormat
METRICS_EXPORT_FORMAT_JSON: MetricsExportFormat
METRICS_EXPORT_FORMAT_CSV: MetricsExportFormat
METRICS_EXPORT_FORMAT_OPENTELEMETRY: MetricsExportFormat
