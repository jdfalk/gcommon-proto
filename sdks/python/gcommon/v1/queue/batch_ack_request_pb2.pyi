from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchAckRequest(_message.Message):
    __slots__ = ("message_ids", "consumer_group_id", "subscription_id", "ack_level", "timeout_ms")
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    consumer_group_id: str
    subscription_id: str
    ack_level: str
    timeout_ms: int
    def __init__(self, message_ids: _Optional[_Iterable[str]] = ..., consumer_group_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., ack_level: _Optional[str] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
