from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteQueueRequest(_message.Message):
    __slots__ = ("queue", "force", "purge_first")
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    PURGE_FIRST_FIELD_NUMBER: _ClassVar[int]
    queue: str
    force: bool
    purge_first: bool
    def __init__(self, queue: _Optional[str] = ..., force: _Optional[bool] = ..., purge_first: _Optional[bool] = ...) -> None: ...
