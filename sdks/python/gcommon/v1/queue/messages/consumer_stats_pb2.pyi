from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerStats(_message.Message):
    __slots__ = ("consumer_id", "messages_processed", "processing_rate", "error_count", "last_active")
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_RATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    consumer_id: str
    messages_processed: int
    processing_rate: float
    error_count: int
    last_active: int
    def __init__(self, consumer_id: _Optional[str] = ..., messages_processed: _Optional[int] = ..., processing_rate: _Optional[float] = ..., error_count: _Optional[int] = ..., last_active: _Optional[int] = ...) -> None: ...
