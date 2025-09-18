from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendMessageResponse(_message.Message):
    __slots__ = ("message_id", "success", "queue_position", "error")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    success: bool
    queue_position: int
    error: _error_pb2.Error
    def __init__(self, message_id: _Optional[str] = ..., success: _Optional[bool] = ..., queue_position: _Optional[int] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
