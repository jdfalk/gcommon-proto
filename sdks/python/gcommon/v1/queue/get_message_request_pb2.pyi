from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetMessageRequest(_message.Message):
    __slots__ = ("topic", "message_id", "partition_id", "offset", "include_metadata", "timeout_ms")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    topic: str
    message_id: str
    partition_id: int
    offset: int
    include_metadata: bool
    timeout_ms: int
    def __init__(self, topic: _Optional[str] = ..., message_id: _Optional[str] = ..., partition_id: _Optional[int] = ..., offset: _Optional[int] = ..., include_metadata: _Optional[bool] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
