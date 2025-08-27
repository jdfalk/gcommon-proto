from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATCH_PRIORITY_UNSPECIFIED: _ClassVar[BatchPriority]
    BATCH_PRIORITY_LOW: _ClassVar[BatchPriority]
    BATCH_PRIORITY_NORMAL: _ClassVar[BatchPriority]
    BATCH_PRIORITY_HIGH: _ClassVar[BatchPriority]
    BATCH_PRIORITY_URGENT: _ClassVar[BatchPriority]

BATCH_PRIORITY_UNSPECIFIED: BatchPriority
BATCH_PRIORITY_LOW: BatchPriority
BATCH_PRIORITY_NORMAL: BatchPriority
BATCH_PRIORITY_HIGH: BatchPriority
BATCH_PRIORITY_URGENT: BatchPriority
