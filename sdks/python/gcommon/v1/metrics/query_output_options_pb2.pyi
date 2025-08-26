from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryOutputOptions(_message.Message):
    __slots__ = ("include_timestamps", "include_labels", "compress_output", "numeric_precision", "include_statistics")
    INCLUDE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LABELS_FIELD_NUMBER: _ClassVar[int]
    COMPRESS_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_PRECISION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    include_timestamps: bool
    include_labels: bool
    compress_output: bool
    numeric_precision: int
    include_statistics: bool
    def __init__(self, include_timestamps: _Optional[bool] = ..., include_labels: _Optional[bool] = ..., compress_output: _Optional[bool] = ..., numeric_precision: _Optional[int] = ..., include_statistics: _Optional[bool] = ...) -> None: ...
