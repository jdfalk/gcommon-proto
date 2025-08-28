from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteQueueResponse(_message.Message):
    __slots__ = ("success", "purged_messages", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PURGED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    purged_messages: int
    message: str
    def __init__(self, success: bool = ..., purged_messages: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
