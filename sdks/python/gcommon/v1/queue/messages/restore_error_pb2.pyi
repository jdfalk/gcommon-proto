from gcommon.v1.queue.messages import offset_range_pb2 as _offset_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreError(_message.Message):
    __slots__ = ("error_code", "error_message", "error_category", "failed_component", "partition_id", "affected_range", "error_time", "recoverable")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FAILED_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_RANGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TIME_FIELD_NUMBER: _ClassVar[int]
    RECOVERABLE_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_message: str
    error_category: str
    failed_component: str
    partition_id: int
    affected_range: _offset_range_pb2.OffsetRange
    error_time: _timestamp_pb2.Timestamp
    recoverable: bool
    def __init__(self, error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., error_category: _Optional[str] = ..., failed_component: _Optional[str] = ..., partition_id: _Optional[int] = ..., affected_range: _Optional[_Union[_offset_range_pb2.OffsetRange, _Mapping]] = ..., error_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., recoverable: bool = ...) -> None: ...
