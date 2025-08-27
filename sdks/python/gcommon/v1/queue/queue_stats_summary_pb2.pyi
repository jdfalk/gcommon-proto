import datetime

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueStatsSummary(_message.Message):
    __slots__ = (
        "total_queues",
        "total_messages",
        "messages_processed_last_hour",
        "average_processing_time",
        "health_score",
        "active_consumers",
        "total_storage_bytes",
    )
    TOTAL_QUEUES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PROCESSED_LAST_HOUR_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_queues: int
    total_messages: int
    messages_processed_last_hour: int
    average_processing_time: _duration_pb2.Duration
    health_score: int
    active_consumers: int
    total_storage_bytes: int
    def __init__(
        self,
        total_queues: _Optional[int] = ...,
        total_messages: _Optional[int] = ...,
        messages_processed_last_hour: _Optional[int] = ...,
        average_processing_time: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        health_score: _Optional[int] = ...,
        active_consumers: _Optional[int] = ...,
        total_storage_bytes: _Optional[int] = ...,
    ) -> None: ...
