import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DequeueResponse(_message.Message):
    __slots__ = (
        "messages",
        "success",
        "request_metadata",
        "queue_name",
        "messages_remaining",
        "approximate_queue_size",
        "consumer_id",
        "wait_started_at",
        "wait_duration_ms",
        "timed_out",
        "error",
        "operation_started_at",
        "response_generated_at",
    )
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATE_QUEUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    WAIT_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    WAIT_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TIMED_OUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    OPERATION_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[
        _queue_message_pb2.QueueMessage
    ]
    success: bool
    request_metadata: _request_metadata_pb2.RequestMetadata
    queue_name: str
    messages_remaining: int
    approximate_queue_size: int
    consumer_id: str
    wait_started_at: _timestamp_pb2.Timestamp
    wait_duration_ms: int
    timed_out: bool
    error: _error_pb2.Error
    operation_started_at: _timestamp_pb2.Timestamp
    response_generated_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        messages: _Optional[
            _Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]
        ] = ...,
        success: _Optional[bool] = ...,
        request_metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        queue_name: _Optional[str] = ...,
        messages_remaining: _Optional[int] = ...,
        approximate_queue_size: _Optional[int] = ...,
        consumer_id: _Optional[str] = ...,
        wait_started_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        wait_duration_ms: _Optional[int] = ...,
        timed_out: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        operation_started_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        response_generated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
