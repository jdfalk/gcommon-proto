from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchNackResponse(_message.Message):
    __slots__ = ("successful_count", "failed_count", "successful_message_ids", "failed_message_ids", "error_messages", "error")
    SUCCESSFUL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCESSFUL_MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    successful_count: int
    failed_count: int
    successful_message_ids: _containers.RepeatedScalarFieldContainer[str]
    failed_message_ids: _containers.RepeatedScalarFieldContainer[str]
    error_messages: _containers.RepeatedScalarFieldContainer[str]
    error: str
    def __init__(self, successful_count: _Optional[int] = ..., failed_count: _Optional[int] = ..., successful_message_ids: _Optional[_Iterable[str]] = ..., failed_message_ids: _Optional[_Iterable[str]] = ..., error_messages: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ...) -> None: ...
