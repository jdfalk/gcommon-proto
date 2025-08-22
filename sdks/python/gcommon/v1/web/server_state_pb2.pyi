from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVER_STATE_UNSPECIFIED: _ClassVar[ServerState]
    SERVER_STATE_STARTING: _ClassVar[ServerState]
    SERVER_STATE_RUNNING: _ClassVar[ServerState]
    SERVER_STATE_STOPPING: _ClassVar[ServerState]
    SERVER_STATE_STOPPED: _ClassVar[ServerState]
SERVER_STATE_UNSPECIFIED: ServerState
SERVER_STATE_STARTING: ServerState
SERVER_STATE_RUNNING: ServerState
SERVER_STATE_STOPPING: ServerState
SERVER_STATE_STOPPED: ServerState
