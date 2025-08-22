from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FailedAck(_message.Message):
    __slots__ = ("message_id", "error_reason", "error_code")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    error_reason: str
    error_code: str
    def __init__(self, message_id: _Optional[str] = ..., error_reason: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
