from gcommon.v1.queue.enums import delivery_mode_pb2 as _delivery_mode_pb2
from gcommon.v1.queue.enums import priority_level_pb2 as _priority_level_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageProperties(_message.Message):
    __slots__ = ("priority", "delivery_mode", "expiration_time", "correlation_id", "reply_to", "content_type", "content_encoding", "compression", "deduplication_id", "delivery_delay_ms")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_MODE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    priority: _priority_level_pb2.PriorityLevel
    delivery_mode: _delivery_mode_pb2.DeliveryMode
    expiration_time: _timestamp_pb2.Timestamp
    correlation_id: str
    reply_to: str
    content_type: str
    content_encoding: str
    compression: str
    deduplication_id: str
    delivery_delay_ms: int
    def __init__(self, priority: _Optional[_Union[_priority_level_pb2.PriorityLevel, str]] = ..., delivery_mode: _Optional[_Union[_delivery_mode_pb2.DeliveryMode, str]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., correlation_id: _Optional[str] = ..., reply_to: _Optional[str] = ..., content_type: _Optional[str] = ..., content_encoding: _Optional[str] = ..., compression: _Optional[str] = ..., deduplication_id: _Optional[str] = ..., delivery_delay_ms: _Optional[int] = ...) -> None: ...
