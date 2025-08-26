from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageUpdateProperties(_message.Message):
    __slots__ = ("expiration_time", "delivery_delay_ms", "retry_count", "routing_key", "correlation_id", "reply_to", "headers")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    expiration_time: _timestamp_pb2.Timestamp
    delivery_delay_ms: int
    retry_count: int
    routing_key: str
    correlation_id: str
    reply_to: str
    headers: _containers.ScalarMap[str, str]
    def __init__(self, expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delivery_delay_ms: _Optional[int] = ..., retry_count: _Optional[int] = ..., routing_key: _Optional[str] = ..., correlation_id: _Optional[str] = ..., reply_to: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
