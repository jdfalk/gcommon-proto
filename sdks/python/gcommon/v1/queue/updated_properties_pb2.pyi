from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatedProperties(_message.Message):
    __slots__ = ("priority_level", "expiration_time", "visibility_timeout_ms", "routing_key", "metadata_count", "headers_count", "content_updated", "content_size_bytes")
    PRIORITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    METADATA_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEADERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_UPDATED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    priority_level: int
    expiration_time: _timestamp_pb2.Timestamp
    visibility_timeout_ms: int
    routing_key: str
    metadata_count: int
    headers_count: int
    content_updated: bool
    content_size_bytes: int
    def __init__(self, priority_level: _Optional[int] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., visibility_timeout_ms: _Optional[int] = ..., routing_key: _Optional[str] = ..., metadata_count: _Optional[int] = ..., headers_count: _Optional[int] = ..., content_updated: bool = ..., content_size_bytes: _Optional[int] = ...) -> None: ...
