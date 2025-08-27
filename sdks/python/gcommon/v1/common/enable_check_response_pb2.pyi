from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnableCheckResponse(_message.Message):
    __slots__ = ("success", "check_id", "error", "status")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    check_id: str
    error: _error_pb2.Error
    status: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        check_id: _Optional[str] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        status: _Optional[str] = ...,
    ) -> None: ...
