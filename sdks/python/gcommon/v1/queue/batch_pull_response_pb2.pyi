from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPullResponse(_message.Message):
    __slots__ = ("messages", "message_count", "has_more", "next_token", "total_bytes")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    message_count: int
    has_more: bool
    next_token: str
    total_bytes: int
    def __init__(self, messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., message_count: _Optional[int] = ..., has_more: bool = ..., next_token: _Optional[str] = ..., total_bytes: _Optional[int] = ...) -> None: ...
