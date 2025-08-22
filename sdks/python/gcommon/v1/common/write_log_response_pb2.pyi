from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WriteLogResponse(_message.Message):
    __slots__ = ("status", "log_id", "error")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    status: str
    log_id: str
    error: str
    def __init__(self, status: _Optional[str] = ..., log_id: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
