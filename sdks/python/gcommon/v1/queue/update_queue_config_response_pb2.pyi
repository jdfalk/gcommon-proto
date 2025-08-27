from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateQueueConfigResponse(_message.Message):
    __slots__ = ("success", "error_message", "config_version", "updated_at", "updated_fields")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    config_version: int
    updated_at: int
    updated_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: _Optional[bool] = ..., error_message: _Optional[str] = ..., config_version: _Optional[int] = ..., updated_at: _Optional[int] = ..., updated_fields: _Optional[_Iterable[str]] = ...) -> None: ...
