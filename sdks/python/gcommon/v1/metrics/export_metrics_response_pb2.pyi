from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportMetricsResponse(_message.Message):
    __slots__ = ("success", "error", "exported_records", "exported_at", "file_url")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_RECORDS_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_AT_FIELD_NUMBER: _ClassVar[int]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    exported_records: int
    exported_at: _timestamp_pb2.Timestamp
    file_url: str
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., exported_records: _Optional[int] = ..., exported_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., file_url: _Optional[str] = ...) -> None: ...
