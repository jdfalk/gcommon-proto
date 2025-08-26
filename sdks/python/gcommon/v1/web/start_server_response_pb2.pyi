from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import server_status_pb2 as _server_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartServerResponse(_message.Message):
    __slots__ = ("success", "status", "listen_address", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LISTEN_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    status: _server_status_pb2.ServerStatus
    listen_address: str
    error: _error_pb2.Error
    def __init__(self, success: bool = ..., status: _Optional[_Union[_server_status_pb2.ServerStatus, str]] = ..., listen_address: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
