from gcommon.v1.queue.messages import message_envelope_pb2 as _message_envelope_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMessageResponse(_message.Message):
    __slots__ = ("message", "ack_token", "has_more", "message_offset", "queue_depth")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    QUEUE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    message: _message_envelope_pb2.MessageEnvelope
    ack_token: str
    has_more: bool
    message_offset: int
    queue_depth: int
    def __init__(self, message: _Optional[_Union[_message_envelope_pb2.MessageEnvelope, _Mapping]] = ..., ack_token: _Optional[str] = ..., has_more: bool = ..., message_offset: _Optional[int] = ..., queue_depth: _Optional[int] = ...) -> None: ...
