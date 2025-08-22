from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PublishResult(_message.Message):
    __slots__ = ("message_id", "success", "error", "partition_id", "offset", "timestamp")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    success: bool
    error: str
    partition_id: int
    offset: int
    timestamp: int
    def __init__(self, message_id: _Optional[str] = ..., success: bool = ..., error: _Optional[str] = ..., partition_id: _Optional[int] = ..., offset: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...
