from gcommon.v1.common import numeric_format_pb2 as _numeric_format_pb2
from gcommon.v1.common import response_compression_pb2 as _response_compression_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OutputOptions(_message.Message):
    __slots__ = ("numeric_format", "include_timestamps", "include_labels", "compression", "flatten_response", "timezone")
    NUMERIC_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LABELS_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    FLATTEN_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    numeric_format: _numeric_format_pb2.NumericFormat
    include_timestamps: bool
    include_labels: bool
    compression: _response_compression_pb2.ResponseCompression
    flatten_response: bool
    timezone: str
    def __init__(self, numeric_format: _Optional[_Union[_numeric_format_pb2.NumericFormat, str]] = ..., include_timestamps: _Optional[bool] = ..., include_labels: _Optional[bool] = ..., compression: _Optional[_Union[_response_compression_pb2.ResponseCompression, str]] = ..., flatten_response: _Optional[bool] = ..., timezone: _Optional[str] = ...) -> None: ...
