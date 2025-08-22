from gcommon.v1.common import error_pb2 as _error_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageAckResult(_message.Message):
    __slots__ = ("receipt_handle", "success", "error", "message_id", "processing_result")
    RECEIPT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_RESULT_FIELD_NUMBER: _ClassVar[int]
    receipt_handle: str
    success: bool
    error: _error_pb2.Error
    message_id: str
    processing_result: str
    def __init__(self, receipt_handle: _Optional[str] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., message_id: _Optional[str] = ..., processing_result: _Optional[str] = ...) -> None: ...
