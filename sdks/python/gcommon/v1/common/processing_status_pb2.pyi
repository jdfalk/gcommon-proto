from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROCESSING_STATUS_UNSPECIFIED: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_PENDING: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_PROCESSING: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_COMPLETED: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_FAILED: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_CANCELLED: _ClassVar[ProcessingStatus]
    PROCESSING_STATUS_PAUSED: _ClassVar[ProcessingStatus]

PROCESSING_STATUS_UNSPECIFIED: ProcessingStatus
PROCESSING_STATUS_PENDING: ProcessingStatus
PROCESSING_STATUS_PROCESSING: ProcessingStatus
PROCESSING_STATUS_COMPLETED: ProcessingStatus
PROCESSING_STATUS_FAILED: ProcessingStatus
PROCESSING_STATUS_CANCELLED: ProcessingStatus
PROCESSING_STATUS_PAUSED: ProcessingStatus
