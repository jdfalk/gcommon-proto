from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteUserResponse(_message.Message):
    __slots__ = ("success", "error_message", "data_retention_info")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_RETENTION_INFO_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    data_retention_info: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        error_message: _Optional[str] = ...,
        data_retention_info: _Optional[str] = ...,
    ) -> None: ...
