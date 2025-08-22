from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUE_TYPE_UNSPECIFIED: _ClassVar[QueueType]
    QUEUE_TYPE_MEMORY: _ClassVar[QueueType]
    QUEUE_TYPE_REDIS: _ClassVar[QueueType]
    QUEUE_TYPE_NATS: _ClassVar[QueueType]
    QUEUE_TYPE_CLOUD: _ClassVar[QueueType]
QUEUE_TYPE_UNSPECIFIED: QueueType
QUEUE_TYPE_MEMORY: QueueType
QUEUE_TYPE_REDIS: QueueType
QUEUE_TYPE_NATS: QueueType
QUEUE_TYPE_CLOUD: QueueType
