from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServerLogsResponse(_message.Message):
    __slots__ = ("success", "request_metadata", "error", "response_generated_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    request_metadata: _request_metadata_pb2.RequestMetadata
    error: _error_pb2.Error
    response_generated_at: _timestamp_pb2.Timestamp
    def __init__(self, success: bool = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., response_generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
