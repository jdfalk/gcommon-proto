from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NackResponse(_message.Message):
    __slots__ = ("success", "error", "message_id", "timestamp")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str
    message_id: str
    timestamp: int
    def __init__(self, success: bool = ..., error: _Optional[str] = ..., message_id: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
