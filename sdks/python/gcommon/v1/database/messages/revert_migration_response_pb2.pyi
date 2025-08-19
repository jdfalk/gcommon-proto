from gcommon.v1.common.messages import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevertMigrationResponse(_message.Message):
    __slots__ = ("success", "reverted_to", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REVERTED_TO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    reverted_to: str
    error: _error_pb2.Error
    def __init__(self, success: bool = ..., reverted_to: _Optional[str] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
