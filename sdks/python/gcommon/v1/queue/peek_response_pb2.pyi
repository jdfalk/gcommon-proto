from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeekResponse(_message.Message):
    __slots__ = ("messages", "success", "request_metadata", "queue_name", "total_matching_messages", "approximate_queue_size", "start_position", "end_position", "has_more_messages", "filtered_message_count", "oldest_message_time", "newest_message_time", "error", "peeked_at", "response_generated_at")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MATCHING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    END_POSITION_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    FILTERED_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    OLDEST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEWEST_MESSAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PEEKED_AT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    success: bool
    request_metadata: _request_metadata_pb2.RequestMetadata
    queue_name: str
    total_matching_messages: int
    approximate_queue_size: int
    start_position: int
    end_position: int
    has_more_messages: bool
    filtered_message_count: int
    oldest_message_time: _timestamp_pb2.Timestamp
    newest_message_time: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    peeked_at: _timestamp_pb2.Timestamp
    response_generated_at: _timestamp_pb2.Timestamp
    def __init__(self, messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., success: bool = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., queue_name: _Optional[str] = ..., total_matching_messages: _Optional[int] = ..., approximate_queue_size: _Optional[int] = ..., start_position: _Optional[int] = ..., end_position: _Optional[int] = ..., has_more_messages: bool = ..., filtered_message_count: _Optional[int] = ..., oldest_message_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., newest_message_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., peeked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
