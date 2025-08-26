from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueConsumerStats(_message.Message):
    __slots__ = ("consumer_id", "queue_name", "messages_processed", "processing_rate", "success_rate", "last_activity", "average_processing_time")
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_RATE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    consumer_id: str
    queue_name: str
    messages_processed: int
    processing_rate: float
    success_rate: float
    last_activity: _timestamp_pb2.Timestamp
    average_processing_time: _duration_pb2.Duration
    def __init__(self, consumer_id: _Optional[str] = ..., queue_name: _Optional[str] = ..., messages_processed: _Optional[int] = ..., processing_rate: _Optional[float] = ..., success_rate: _Optional[float] = ..., last_activity: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., average_processing_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
