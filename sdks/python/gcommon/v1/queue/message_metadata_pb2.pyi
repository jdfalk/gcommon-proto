import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageMetadata(_message.Message):
    __slots__ = ("message_id", "timestamp", "producer_id", "content_type", "content_encoding", "priority", "ttl_ms", "headers", "routing_key", "correlation_id", "reply_to")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TTL_MS_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    timestamp: _timestamp_pb2.Timestamp
    producer_id: str
    content_type: str
    content_encoding: str
    priority: int
    ttl_ms: int
    headers: _containers.ScalarMap[str, str]
    routing_key: str
    correlation_id: str
    reply_to: str
    def __init__(self, message_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., producer_id: _Optional[str] = ..., content_type: _Optional[str] = ..., content_encoding: _Optional[str] = ..., priority: _Optional[int] = ..., ttl_ms: _Optional[int] = ..., headers: _Optional[_Mapping[str, str]] = ..., routing_key: _Optional[str] = ..., correlation_id: _Optional[str] = ..., reply_to: _Optional[str] = ...) -> None: ...
