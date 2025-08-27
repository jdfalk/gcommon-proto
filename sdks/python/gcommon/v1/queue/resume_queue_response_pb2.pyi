import datetime

from gcommon.v1.common import queue_state_pb2 as _queue_state_pb2
from gcommon.v1.queue import resume_stats_pb2 as _resume_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResumeQueueResponse(_message.Message):
    __slots__ = ("success", "queue_id", "previous_state", "current_state", "resumed_at", "pause_duration_ms", "messages_queued_during_pause", "affected_consumer_groups", "error_message", "error_code", "warnings", "resume_stats", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    RESUMED_AT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_QUEUED_DURING_PAUSE_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_CONSUMER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    RESUME_STATS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    queue_id: str
    previous_state: _queue_state_pb2.QueueState
    current_state: _queue_state_pb2.QueueState
    resumed_at: _timestamp_pb2.Timestamp
    pause_duration_ms: int
    messages_queued_during_pause: int
    affected_consumer_groups: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    error_code: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    resume_stats: _resume_stats_pb2.ResumeStats
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, success: _Optional[bool] = ..., queue_id: _Optional[str] = ..., previous_state: _Optional[_Union[_queue_state_pb2.QueueState, str]] = ..., current_state: _Optional[_Union[_queue_state_pb2.QueueState, str]] = ..., resumed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pause_duration_ms: _Optional[int] = ..., messages_queued_during_pause: _Optional[int] = ..., affected_consumer_groups: _Optional[_Iterable[str]] = ..., error_message: _Optional[str] = ..., error_code: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ..., resume_stats: _Optional[_Union[_resume_stats_pb2.ResumeStats, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
