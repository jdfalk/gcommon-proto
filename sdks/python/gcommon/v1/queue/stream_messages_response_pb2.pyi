from gcommon.v1.queue import queue_message_pb2 as _queue_message_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreamMessagesResponse(_message.Message):
    __slots__ = ("messages", "has_more", "continuation_token", "total_messages", "stream_position", "stream_ended")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    STREAM_POSITION_FIELD_NUMBER: _ClassVar[int]
    STREAM_ENDED_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_queue_message_pb2.QueueMessage]
    has_more: bool
    continuation_token: str
    total_messages: int
    stream_position: int
    stream_ended: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[_queue_message_pb2.QueueMessage, _Mapping]]] = ..., has_more: bool = ..., continuation_token: _Optional[str] = ..., total_messages: _Optional[int] = ..., stream_position: _Optional[int] = ..., stream_ended: bool = ...) -> None: ...
