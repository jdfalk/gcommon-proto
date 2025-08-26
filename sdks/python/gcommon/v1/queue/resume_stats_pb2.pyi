from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResumeStats(_message.Message):
    __slots__ = ("partitions_resumed", "subscriptions_reactivated", "consumers_reconnected", "resume_time_ms", "immediate_messages_processed", "post_resume_throughput")
    PARTITIONS_RESUMED_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_REACTIVATED_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_RECONNECTED_FIELD_NUMBER: _ClassVar[int]
    RESUME_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_MESSAGES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    POST_RESUME_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    partitions_resumed: int
    subscriptions_reactivated: int
    consumers_reconnected: int
    resume_time_ms: int
    immediate_messages_processed: int
    post_resume_throughput: float
    def __init__(self, partitions_resumed: _Optional[int] = ..., subscriptions_reactivated: _Optional[int] = ..., consumers_reconnected: _Optional[int] = ..., resume_time_ms: _Optional[int] = ..., immediate_messages_processed: _Optional[int] = ..., post_resume_throughput: _Optional[float] = ...) -> None: ...
