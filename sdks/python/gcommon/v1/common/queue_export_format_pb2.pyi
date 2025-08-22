from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueExportFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUE_EXPORT_FORMAT_UNSPECIFIED: _ClassVar[QueueExportFormat]
    QUEUE_EXPORT_FORMAT_JSON: _ClassVar[QueueExportFormat]
    QUEUE_EXPORT_FORMAT_PROTOBUF: _ClassVar[QueueExportFormat]
    QUEUE_EXPORT_FORMAT_CSV: _ClassVar[QueueExportFormat]
    QUEUE_EXPORT_FORMAT_CUSTOM: _ClassVar[QueueExportFormat]
QUEUE_EXPORT_FORMAT_UNSPECIFIED: QueueExportFormat
QUEUE_EXPORT_FORMAT_JSON: QueueExportFormat
QUEUE_EXPORT_FORMAT_PROTOBUF: QueueExportFormat
QUEUE_EXPORT_FORMAT_CSV: QueueExportFormat
QUEUE_EXPORT_FORMAT_CUSTOM: QueueExportFormat
