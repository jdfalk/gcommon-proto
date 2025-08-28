from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.queue import message_ack_result_pb2 as _message_ack_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcknowledgeResponse(_message.Message):
    __slots__ = ("success", "acknowledged_count", "failed_count", "request_metadata", "queue_name", "message_results", "consumer_id", "operation_time_ms", "batch_mode", "already_acknowledged_count", "expired_timeout_count", "error", "acknowledged_at", "response_generated_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    ALREADY_ACKNOWLEDGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_TIMEOUT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGED_AT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    acknowledged_count: int
    failed_count: int
    request_metadata: _request_metadata_pb2.RequestMetadata
    queue_name: str
    message_results: _containers.RepeatedCompositeFieldContainer[_message_ack_result_pb2.MessageAckResult]
    consumer_id: str
    operation_time_ms: int
    batch_mode: bool
    already_acknowledged_count: int
    expired_timeout_count: int
    error: _error_pb2.Error
    acknowledged_at: _timestamp_pb2.Timestamp
    response_generated_at: _timestamp_pb2.Timestamp
    def __init__(self, success: bool = ..., acknowledged_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., queue_name: _Optional[str] = ..., message_results: _Optional[_Iterable[_Union[_message_ack_result_pb2.MessageAckResult, _Mapping]]] = ..., consumer_id: _Optional[str] = ..., operation_time_ms: _Optional[int] = ..., batch_mode: bool = ..., already_acknowledged_count: _Optional[int] = ..., expired_timeout_count: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., acknowledged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
