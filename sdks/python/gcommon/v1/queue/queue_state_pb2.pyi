from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUE_STATE_UNSPECIFIED: _ClassVar[QueueState]
    QUEUE_STATE_ACTIVE: _ClassVar[QueueState]
    QUEUE_STATE_PAUSED: _ClassVar[QueueState]
    QUEUE_STATE_SUSPENDED: _ClassVar[QueueState]
    QUEUE_STATE_DELETING: _ClassVar[QueueState]
    QUEUE_STATE_MAINTENANCE: _ClassVar[QueueState]
    QUEUE_STATE_ERROR: _ClassVar[QueueState]
QUEUE_STATE_UNSPECIFIED: QueueState
QUEUE_STATE_ACTIVE: QueueState
QUEUE_STATE_PAUSED: QueueState
QUEUE_STATE_SUSPENDED: QueueState
QUEUE_STATE_DELETING: QueueState
QUEUE_STATE_MAINTENANCE: QueueState
QUEUE_STATE_ERROR: QueueState
