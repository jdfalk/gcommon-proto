from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeadLetterQueueConfig(_message.Message):
    __slots__ = ("enabled", "dlq_topic", "dlq_max_age_seconds", "include_error_info")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DLQ_TOPIC_FIELD_NUMBER: _ClassVar[int]
    DLQ_MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    dlq_topic: str
    dlq_max_age_seconds: int
    include_error_info: bool
    def __init__(self, enabled: bool = ..., dlq_topic: _Optional[str] = ..., dlq_max_age_seconds: _Optional[int] = ..., include_error_info: bool = ...) -> None: ...
