from gcommon.v1.queue import consumer_error_stats_pb2 as _consumer_error_stats_pb2
from gcommon.v1.queue import rebalance_stats_pb2 as _rebalance_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerGroupStats(_message.Message):
    __slots__ = ("active_consumers", "assigned_partitions", "total_messages_consumed", "total_bytes_consumed", "group_consumption_rate", "total_lag", "rebalance_stats", "error_stats")
    ACTIVE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MESSAGES_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONSUMPTION_RATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LAG_FIELD_NUMBER: _ClassVar[int]
    REBALANCE_STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATS_FIELD_NUMBER: _ClassVar[int]
    active_consumers: int
    assigned_partitions: int
    total_messages_consumed: int
    total_bytes_consumed: int
    group_consumption_rate: float
    total_lag: int
    rebalance_stats: _rebalance_stats_pb2.RebalanceStats
    error_stats: _consumer_error_stats_pb2.ConsumerErrorStats
    def __init__(self, active_consumers: _Optional[int] = ..., assigned_partitions: _Optional[int] = ..., total_messages_consumed: _Optional[int] = ..., total_bytes_consumed: _Optional[int] = ..., group_consumption_rate: _Optional[float] = ..., total_lag: _Optional[int] = ..., rebalance_stats: _Optional[_Union[_rebalance_stats_pb2.RebalanceStats, _Mapping]] = ..., error_stats: _Optional[_Union[_consumer_error_stats_pb2.ConsumerErrorStats, _Mapping]] = ...) -> None: ...
