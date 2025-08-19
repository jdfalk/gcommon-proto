from gcommon.v1.queue.enums import nack_error_category_pb2 as _nack_error_category_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NackError(_message.Message):
    __slots__ = ("code", "message", "category", "retryable", "details")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    category: _nack_error_category_pb2.NackErrorCategory
    retryable: bool
    details: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., category: _Optional[_Union[_nack_error_category_pb2.NackErrorCategory, str]] = ..., retryable: bool = ..., details: _Optional[str] = ...) -> None: ...
