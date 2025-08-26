from gcommon.v1.queue import message_nack_pb2 as _message_nack_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchNackRequest(_message.Message):
    __slots__ = ("consumer_group_id", "consumer_id", "message_nacks", "requeue_messages", "requeue_delay_ms", "max_requeue_attempts", "send_to_dlq", "nack_reason", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_NACKS_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    REQUEUE_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEUE_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    SEND_TO_DLQ_FIELD_NUMBER: _ClassVar[int]
    NACK_REASON_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    consumer_group_id: str
    consumer_id: str
    message_nacks: _containers.RepeatedCompositeFieldContainer[_message_nack_pb2.MessageNack]
    requeue_messages: bool
    requeue_delay_ms: int
    max_requeue_attempts: int
    send_to_dlq: bool
    nack_reason: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, consumer_group_id: _Optional[str] = ..., consumer_id: _Optional[str] = ..., message_nacks: _Optional[_Iterable[_Union[_message_nack_pb2.MessageNack, _Mapping]]] = ..., requeue_messages: _Optional[bool] = ..., requeue_delay_ms: _Optional[int] = ..., max_requeue_attempts: _Optional[int] = ..., send_to_dlq: _Optional[bool] = ..., nack_reason: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
