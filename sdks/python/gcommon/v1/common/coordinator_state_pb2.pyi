from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CoordinatorState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COORDINATOR_STATE_UNSPECIFIED: _ClassVar[CoordinatorState]
    COORDINATOR_STATE_ACTIVE: _ClassVar[CoordinatorState]
    COORDINATOR_STATE_LOADING: _ClassVar[CoordinatorState]
    COORDINATOR_STATE_NOT_COORDINATOR: _ClassVar[CoordinatorState]
COORDINATOR_STATE_UNSPECIFIED: CoordinatorState
COORDINATOR_STATE_ACTIVE: CoordinatorState
COORDINATOR_STATE_LOADING: CoordinatorState
COORDINATOR_STATE_NOT_COORDINATOR: CoordinatorState
