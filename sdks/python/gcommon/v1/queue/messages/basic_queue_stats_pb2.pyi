from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BasicQueueStats(_message.Message):
    __slots__ = ("queue_name", "total_messages", "unacked_messages", "size_bytes", "consumer_count", "producer_count", "ingress_rate", "egress_rate", "avg_message_size", "queue_depth_ms")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    UNACKED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_COUNT_FIELD_NUMBER: _ClassVar[int]
    INGRESS_RATE_FIELD_NUMBER: _ClassVar[int]
    EGRESS_RATE_FIELD_NUMBER: _ClassVar[int]
    AVG_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_DEPTH_MS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    total_messages: int
    unacked_messages: int
    size_bytes: int
    consumer_count: int
    producer_count: int
    ingress_rate: float
    egress_rate: float
    avg_message_size: float
    queue_depth_ms: int
    def __init__(self, queue_name: _Optional[str] = ..., total_messages: _Optional[int] = ..., unacked_messages: _Optional[int] = ..., size_bytes: _Optional[int] = ..., consumer_count: _Optional[int] = ..., producer_count: _Optional[int] = ..., ingress_rate: _Optional[float] = ..., egress_rate: _Optional[float] = ..., avg_message_size: _Optional[float] = ..., queue_depth_ms: _Optional[int] = ...) -> None: ...
