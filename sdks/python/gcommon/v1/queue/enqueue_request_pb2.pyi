import datetime

from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnqueueRequest(_message.Message):
    __slots__ = ("queue_name", "payload", "metadata", "priority", "delay", "expires_at", "group_id", "deduplication_id", "max_delivery_attempts", "attributes", "content_type", "source", "message_type", "correlation_id", "reply_to")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DELIVERY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    payload: _any_pb2.Any
    metadata: _request_metadata_pb2.RequestMetadata
    priority: int
    delay: _duration_pb2.Duration
    expires_at: _timestamp_pb2.Timestamp
    group_id: str
    deduplication_id: str
    max_delivery_attempts: int
    attributes: _containers.ScalarMap[str, str]
    content_type: str
    source: str
    message_type: str
    correlation_id: str
    reply_to: str
    def __init__(self, queue_name: _Optional[str] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., priority: _Optional[int] = ..., delay: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., group_id: _Optional[str] = ..., deduplication_id: _Optional[str] = ..., max_delivery_attempts: _Optional[int] = ..., attributes: _Optional[_Mapping[str, str]] = ..., content_type: _Optional[str] = ..., source: _Optional[str] = ..., message_type: _Optional[str] = ..., correlation_id: _Optional[str] = ..., reply_to: _Optional[str] = ...) -> None: ...
