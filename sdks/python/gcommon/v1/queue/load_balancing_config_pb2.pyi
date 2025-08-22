from gcommon.v1.queue import load_balancing_strategy_pb2 as _load_balancing_strategy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadBalancingConfig(_message.Message):
    __slots__ = ("strategy", "weight", "max_concurrent_messages", "prefetch_count", "priority", "sticky_sessions", "affinity_key")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    STICKY_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    AFFINITY_KEY_FIELD_NUMBER: _ClassVar[int]
    strategy: _load_balancing_strategy_pb2.LoadBalancingStrategy
    weight: int
    max_concurrent_messages: int
    prefetch_count: int
    priority: int
    sticky_sessions: bool
    affinity_key: str
    def __init__(self, strategy: _Optional[_Union[_load_balancing_strategy_pb2.LoadBalancingStrategy, str]] = ..., weight: _Optional[int] = ..., max_concurrent_messages: _Optional[int] = ..., prefetch_count: _Optional[int] = ..., priority: _Optional[int] = ..., sticky_sessions: bool = ..., affinity_key: _Optional[str] = ...) -> None: ...
