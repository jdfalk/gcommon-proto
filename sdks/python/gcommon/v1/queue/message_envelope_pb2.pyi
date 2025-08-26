import datetime

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageEnvelope(_message.Message):
    __slots__ = ("message_id", "payload", "headers", "priority", "created_at", "process_at", "expires_at", "delivery_count", "correlation_id", "reply_to", "content_type", "content_encoding", "requires_ack", "trace_context")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TraceContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    PROCESS_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_ACK_FIELD_NUMBER: _ClassVar[int]
    TRACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    payload: _any_pb2.Any
    headers: _containers.ScalarMap[str, str]
    priority: int
    created_at: _timestamp_pb2.Timestamp
    process_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    delivery_count: int
    correlation_id: str
    reply_to: str
    content_type: str
    content_encoding: str
    requires_ack: bool
    trace_context: _containers.ScalarMap[str, str]
    def __init__(self, message_id: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., headers: _Optional[_Mapping[str, str]] = ..., priority: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., process_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_count: _Optional[int] = ..., correlation_id: _Optional[str] = ..., reply_to: _Optional[str] = ..., content_type: _Optional[str] = ..., content_encoding: _Optional[str] = ..., requires_ack: _Optional[bool] = ..., trace_context: _Optional[_Mapping[str, str]] = ...) -> None: ...
