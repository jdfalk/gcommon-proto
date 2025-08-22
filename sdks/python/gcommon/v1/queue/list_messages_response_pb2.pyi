from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMessagesResponse(_message.Message):
    __slots__ = ("messages", "total_count", "next_page_token", "has_more", "error")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    total_count: int
    next_page_token: str
    has_more: bool
    error: str
    def __init__(self, messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., total_count: _Optional[int] = ..., next_page_token: _Optional[str] = ..., has_more: bool = ..., error: _Optional[str] = ...) -> None: ...
