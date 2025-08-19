from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class NodeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_STATE_UNSPECIFIED: _ClassVar[NodeState]
    NODE_STATE_ACTIVE: _ClassVar[NodeState]
    NODE_STATE_INACTIVE: _ClassVar[NodeState]
    NODE_STATE_UNREACHABLE: _ClassVar[NodeState]
    NODE_STATE_JOINING: _ClassVar[NodeState]
    NODE_STATE_LEAVING: _ClassVar[NodeState]
NODE_STATE_UNSPECIFIED: NodeState
NODE_STATE_ACTIVE: NodeState
NODE_STATE_INACTIVE: NodeState
NODE_STATE_UNREACHABLE: NodeState
NODE_STATE_JOINING: NodeState
NODE_STATE_LEAVING: NodeState
