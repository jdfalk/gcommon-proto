from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnqueueResponse(_message.Message):
    __slots__ = ("message_id", "success", "request_metadata", "queue_name", "payload_md5", "message_size", "sequence_number", "assigned_priority", "deduplication_id", "group_id", "available_at", "expires_at", "error", "enqueued_at", "response_generated_at")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_MD5_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ENQUEUED_AT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    success: bool
    request_metadata: _request_metadata_pb2.RequestMetadata
    queue_name: str
    payload_md5: str
    message_size: int
    sequence_number: int
    assigned_priority: int
    deduplication_id: str
    group_id: str
    available_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    enqueued_at: _timestamp_pb2.Timestamp
    response_generated_at: _timestamp_pb2.Timestamp
    def __init__(self, message_id: _Optional[str] = ..., success: bool = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., queue_name: _Optional[str] = ..., payload_md5: _Optional[str] = ..., message_size: _Optional[int] = ..., sequence_number: _Optional[int] = ..., assigned_priority: _Optional[int] = ..., deduplication_id: _Optional[str] = ..., group_id: _Optional[str] = ..., available_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., enqueued_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
