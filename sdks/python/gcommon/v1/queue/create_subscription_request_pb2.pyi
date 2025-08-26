from gcommon.v1.queue import subscription_config_pb2 as _subscription_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubscriptionRequest(_message.Message):
    __slots__ = ("subscription_name", "topic", "consumer_group_id", "config", "start_position", "start_offset", "timeout_ms")
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    subscription_name: str
    topic: str
    consumer_group_id: str
    config: _subscription_config_pb2.SubscriptionConfig
    start_position: str
    start_offset: int
    timeout_ms: int
    def __init__(self, subscription_name: _Optional[str] = ..., topic: _Optional[str] = ..., consumer_group_id: _Optional[str] = ..., config: _Optional[_Union[_subscription_config_pb2.SubscriptionConfig, _Mapping]] = ..., start_position: _Optional[str] = ..., start_offset: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
