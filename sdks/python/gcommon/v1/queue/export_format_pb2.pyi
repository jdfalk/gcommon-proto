from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_FORMAT_UNSPECIFIED: _ClassVar[QueueExportFormat]
    EXPORT_FORMAT_JSON: _ClassVar[QueueExportFormat]
    EXPORT_FORMAT_PROTOBUF: _ClassVar[QueueExportFormat]
    EXPORT_FORMAT_CSV: _ClassVar[QueueExportFormat]
    EXPORT_FORMAT_CUSTOM: _ClassVar[QueueExportFormat]
EXPORT_FORMAT_UNSPECIFIED: QueueExportFormat
EXPORT_FORMAT_JSON: QueueExportFormat
EXPORT_FORMAT_PROTOBUF: QueueExportFormat
EXPORT_FORMAT_CSV: QueueExportFormat
EXPORT_FORMAT_CUSTOM: QueueExportFormat
