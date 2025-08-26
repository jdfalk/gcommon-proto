import datetime

from gcommon.v1.common import ack_type_pb2 as _ack_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Acknowledgment(_message.Message):
    __slots__ = ("message_id", "consumer_id", "queue_name", "partition_id", "offset", "ack_type", "ack_timestamp", "processing_duration_ms", "error_message", "retry_count")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACK_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    consumer_id: str
    queue_name: str
    partition_id: int
    offset: int
    ack_type: _ack_type_pb2.AckType
    ack_timestamp: _timestamp_pb2.Timestamp
    processing_duration_ms: int
    error_message: str
    retry_count: int
    def __init__(self, message_id: _Optional[str] = ..., consumer_id: _Optional[str] = ..., queue_name: _Optional[str] = ..., partition_id: _Optional[int] = ..., offset: _Optional[int] = ..., ack_type: _Optional[_Union[_ack_type_pb2.AckType, str]] = ..., ack_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., processing_duration_ms: _Optional[int] = ..., error_message: _Optional[str] = ..., retry_count: _Optional[int] = ...) -> None: ...
