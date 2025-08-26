from gcommon.v1.common import coordinator_state_pb2 as _coordinator_state_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupCoordinator(_message.Message):
    __slots__ = ("node_id", "host", "port", "state", "epoch")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    host: str
    port: int
    state: _coordinator_state_pb2.CoordinatorState
    epoch: int
    def __init__(self, node_id: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ..., state: _Optional[_Union[_coordinator_state_pb2.CoordinatorState, str]] = ..., epoch: _Optional[int] = ...) -> None: ...
