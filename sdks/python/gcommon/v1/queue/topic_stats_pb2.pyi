from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicStats(_message.Message):
    __slots__ = (
        "topic_name",
        "total_messages",
        "total_size_bytes",
        "subscription_count",
        "producer_count",
        "messages_per_second",
        "bytes_per_second",
        "last_message_time",
        "average_message_size",
    )
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    BYTES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    total_messages: int
    total_size_bytes: int
    subscription_count: int
    producer_count: int
    messages_per_second: float
    bytes_per_second: float
    last_message_time: int
    average_message_size: float
    def __init__(
        self,
        topic_name: _Optional[str] = ...,
        total_messages: _Optional[int] = ...,
        total_size_bytes: _Optional[int] = ...,
        subscription_count: _Optional[int] = ...,
        producer_count: _Optional[int] = ...,
        messages_per_second: _Optional[float] = ...,
        bytes_per_second: _Optional[float] = ...,
        last_message_time: _Optional[int] = ...,
        average_message_size: _Optional[float] = ...,
    ) -> None: ...
