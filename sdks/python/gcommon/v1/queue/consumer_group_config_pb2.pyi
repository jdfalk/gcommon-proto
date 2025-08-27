from gcommon.v1.common import load_balancing_strategy_pb2 as _load_balancing_strategy_pb2
from gcommon.v1.common import offset_reset_strategy_pb2 as _offset_reset_strategy_pb2
from gcommon.v1.common import rebalance_strategy_pb2 as _rebalance_strategy_pb2
from gcommon.v1.queue import auto_commit_config_pb2 as _auto_commit_config_pb2
from gcommon.v1.queue import dead_letter_queue_config_pb2 as _dead_letter_queue_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerGroupConfig(_message.Message):
    __slots__ = ("load_balancing_strategy", "rebalance_strategy", "session_timeout_ms", "heartbeat_interval_ms", "max_poll_interval_ms", "auto_commit", "offset_reset_strategy", "max_consumers", "exactly_once_enabled", "dlq_config")
    LOAD_BALANCING_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SESSION_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_POLL_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    AUTO_COMMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_RESET_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    MAX_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    EXACTLY_ONCE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DLQ_CONFIG_FIELD_NUMBER: _ClassVar[int]
    load_balancing_strategy: _load_balancing_strategy_pb2.LoadBalancingStrategy
    rebalance_strategy: _rebalance_strategy_pb2.RebalanceStrategy
    session_timeout_ms: int
    heartbeat_interval_ms: int
    max_poll_interval_ms: int
    auto_commit: _auto_commit_config_pb2.AutoCommitConfig
    offset_reset_strategy: _offset_reset_strategy_pb2.OffsetResetStrategy
    max_consumers: int
    exactly_once_enabled: bool
    dlq_config: _dead_letter_queue_config_pb2.DeadLetterQueueConfig
    def __init__(self, load_balancing_strategy: _Optional[_Union[_load_balancing_strategy_pb2.LoadBalancingStrategy, str]] = ..., rebalance_strategy: _Optional[_Union[_rebalance_strategy_pb2.RebalanceStrategy, str]] = ..., session_timeout_ms: _Optional[int] = ..., heartbeat_interval_ms: _Optional[int] = ..., max_poll_interval_ms: _Optional[int] = ..., auto_commit: _Optional[_Union[_auto_commit_config_pb2.AutoCommitConfig, _Mapping]] = ..., offset_reset_strategy: _Optional[_Union[_offset_reset_strategy_pb2.OffsetResetStrategy, str]] = ..., max_consumers: _Optional[int] = ..., exactly_once_enabled: _Optional[bool] = ..., dlq_config: _Optional[_Union[_dead_letter_queue_config_pb2.DeadLetterQueueConfig, _Mapping]] = ...) -> None: ...
