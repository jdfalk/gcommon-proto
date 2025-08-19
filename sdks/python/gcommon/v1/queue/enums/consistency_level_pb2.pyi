from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class QueueConsistencyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSISTENCY_LEVEL_UNSPECIFIED: _ClassVar[QueueConsistencyLevel]
    CONSISTENCY_LEVEL_EVENTUAL: _ClassVar[QueueConsistencyLevel]
    CONSISTENCY_LEVEL_WEAK: _ClassVar[QueueConsistencyLevel]
    CONSISTENCY_LEVEL_STRONG: _ClassVar[QueueConsistencyLevel]
    CONSISTENCY_LEVEL_SEQUENTIAL: _ClassVar[QueueConsistencyLevel]
    CONSISTENCY_LEVEL_LINEARIZABLE: _ClassVar[QueueConsistencyLevel]
CONSISTENCY_LEVEL_UNSPECIFIED: QueueConsistencyLevel
CONSISTENCY_LEVEL_EVENTUAL: QueueConsistencyLevel
CONSISTENCY_LEVEL_WEAK: QueueConsistencyLevel
CONSISTENCY_LEVEL_STRONG: QueueConsistencyLevel
CONSISTENCY_LEVEL_SEQUENTIAL: QueueConsistencyLevel
CONSISTENCY_LEVEL_LINEARIZABLE: QueueConsistencyLevel
