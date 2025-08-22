from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ServerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVER_STATUS_UNSPECIFIED: _ClassVar[ServerStatus]
    SERVER_STATUS_CREATED: _ClassVar[ServerStatus]
    SERVER_STATUS_STARTING: _ClassVar[ServerStatus]
    SERVER_STATUS_RUNNING: _ClassVar[ServerStatus]
    SERVER_STATUS_STOPPING: _ClassVar[ServerStatus]
    SERVER_STATUS_STOPPED: _ClassVar[ServerStatus]
    SERVER_STATUS_ERROR: _ClassVar[ServerStatus]
SERVER_STATUS_UNSPECIFIED: ServerStatus
SERVER_STATUS_CREATED: ServerStatus
SERVER_STATUS_STARTING: ServerStatus
SERVER_STATUS_RUNNING: ServerStatus
SERVER_STATUS_STOPPING: ServerStatus
SERVER_STATUS_STOPPED: ServerStatus
SERVER_STATUS_ERROR: ServerStatus
