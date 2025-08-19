from gcommon.v1.queue.messages import offset_range_pb2 as _offset_range_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationError(_message.Message):
    __slots__ = ("error_type", "description", "partition_id", "affected_range")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    AFFECTED_RANGE_FIELD_NUMBER: _ClassVar[int]
    error_type: str
    description: str
    partition_id: int
    affected_range: _offset_range_pb2.OffsetRange
    def __init__(self, error_type: _Optional[str] = ..., description: _Optional[str] = ..., partition_id: _Optional[int] = ..., affected_range: _Optional[_Union[_offset_range_pb2.OffsetRange, _Mapping]] = ...) -> None: ...
