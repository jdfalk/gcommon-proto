from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublishResponse(_message.Message):
    __slots__ = ("message_id", "success", "error", "request_metadata")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    success: bool
    error: _error_pb2.Error
    request_metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, message_id: _Optional[str] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
