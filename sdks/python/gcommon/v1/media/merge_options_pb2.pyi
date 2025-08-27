from gcommon.v1.common import conflict_resolution_pb2 as _conflict_resolution_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MergeOptions(_message.Message):
    __slots__ = (
        "output_format",
        "preserve_formatting",
        "conflict_resolution",
        "sort_by_timestamp",
    )
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_FORMATTING_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    output_format: str
    preserve_formatting: bool
    conflict_resolution: _conflict_resolution_pb2.ConflictResolution
    sort_by_timestamp: bool
    def __init__(
        self,
        output_format: _Optional[str] = ...,
        preserve_formatting: _Optional[bool] = ...,
        conflict_resolution: _Optional[
            _Union[_conflict_resolution_pb2.ConflictResolution, str]
        ] = ...,
        sort_by_timestamp: _Optional[bool] = ...,
    ) -> None: ...
