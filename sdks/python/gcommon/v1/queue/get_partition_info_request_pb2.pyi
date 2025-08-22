from gcommon.v1.queue import time_range_filter_pb2 as _time_range_filter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPartitionInfoRequest(_message.Message):
    __slots__ = ("topic_id", "partition_ids", "include_stats", "include_consumers", "include_offsets", "include_health_status", "include_leader_info", "include_config", "time_range", "access_token")
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LEADER_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    include_stats: bool
    include_consumers: bool
    include_offsets: bool
    include_health_status: bool
    include_leader_info: bool
    include_config: bool
    time_range: _time_range_filter_pb2.TimeRangeFilter
    access_token: str
    def __init__(self, topic_id: _Optional[str] = ..., partition_ids: _Optional[_Iterable[int]] = ..., include_stats: bool = ..., include_consumers: bool = ..., include_offsets: bool = ..., include_health_status: bool = ..., include_leader_info: bool = ..., include_config: bool = ..., time_range: _Optional[_Union[_time_range_filter_pb2.TimeRangeFilter, _Mapping]] = ..., access_token: _Optional[str] = ...) -> None: ...
