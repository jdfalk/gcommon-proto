from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CommonExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_FORMAT_UNSPECIFIED: _ClassVar[CommonExportFormat]
    EXPORT_FORMAT_PROMETHEUS: _ClassVar[CommonExportFormat]
    EXPORT_FORMAT_JSON: _ClassVar[CommonExportFormat]
    EXPORT_FORMAT_CSV: _ClassVar[CommonExportFormat]
    EXPORT_FORMAT_OPENTELEMETRY: _ClassVar[CommonExportFormat]

EXPORT_FORMAT_UNSPECIFIED: CommonExportFormat
EXPORT_FORMAT_PROMETHEUS: CommonExportFormat
EXPORT_FORMAT_JSON: CommonExportFormat
EXPORT_FORMAT_CSV: CommonExportFormat
EXPORT_FORMAT_OPENTELEMETRY: CommonExportFormat
