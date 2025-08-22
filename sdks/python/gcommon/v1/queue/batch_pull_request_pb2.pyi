from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchPullRequest(_message.Message):
    __slots__ = ("queue_name", "max_messages", "wait_timeout", "auto_acknowledge", "consumer_group", "subscription", "max_payload_size")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WAIT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    AUTO_ACKNOWLEDGE_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MAX_PAYLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    max_messages: int
    wait_timeout: _duration_pb2.Duration
    auto_acknowledge: bool
    consumer_group: str
    subscription: str
    max_payload_size: int
    def __init__(self, queue_name: _Optional[str] = ..., max_messages: _Optional[int] = ..., wait_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., auto_acknowledge: bool = ..., consumer_group: _Optional[str] = ..., subscription: _Optional[str] = ..., max_payload_size: _Optional[int] = ...) -> None: ...
