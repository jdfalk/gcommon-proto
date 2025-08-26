from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ListMessagesRequest(_message.Message):
    __slots__ = ("topic", "partition_id", "start_offset", "limit", "include_headers", "include_metadata", "status_filter", "timeout_ms")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEADERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    topic: str
    partition_id: int
    start_offset: int
    limit: int
    include_headers: bool
    include_metadata: bool
    status_filter: str
    timeout_ms: int
    def __init__(self, topic: _Optional[str] = ..., partition_id: _Optional[int] = ..., start_offset: _Optional[int] = ..., limit: _Optional[int] = ..., include_headers: _Optional[bool] = ..., include_metadata: _Optional[bool] = ..., status_filter: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
