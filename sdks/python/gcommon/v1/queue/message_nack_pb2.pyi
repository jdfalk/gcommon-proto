from gcommon.v1.common import nack_error_category_pb2 as _nack_error_category_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageNack(_message.Message):
    __slots__ = ("message_id", "delivery_tag", "partition_id", "message_offset", "nack_reason", "error_category", "error_code", "retry_message", "retry_delay_ms", "message_metadata")
    class MessageMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TAG_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    NACK_REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    RETRY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRY_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    delivery_tag: str
    partition_id: int
    message_offset: int
    nack_reason: str
    error_category: _nack_error_category_pb2.NackErrorCategory
    error_code: str
    retry_message: bool
    retry_delay_ms: int
    message_metadata: _containers.ScalarMap[str, str]
    def __init__(self, message_id: _Optional[str] = ..., delivery_tag: _Optional[str] = ..., partition_id: _Optional[int] = ..., message_offset: _Optional[int] = ..., nack_reason: _Optional[str] = ..., error_category: _Optional[_Union[_nack_error_category_pb2.NackErrorCategory, str]] = ..., error_code: _Optional[str] = ..., retry_message: _Optional[bool] = ..., retry_delay_ms: _Optional[int] = ..., message_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
