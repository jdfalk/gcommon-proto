from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PauseQueueResponse(_message.Message):
    __slots__ = ("success", "queue_name", "pause_status", "affected_consumers", "pause_timestamp", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAUSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    queue_name: str
    pause_status: str
    affected_consumers: int
    pause_timestamp: int
    error: str
    def __init__(self, success: _Optional[bool] = ..., queue_name: _Optional[str] = ..., pause_status: _Optional[str] = ..., affected_consumers: _Optional[int] = ..., pause_timestamp: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
