import datetime

from gcommon.v1.common import consumer_group_state_pb2 as _consumer_group_state_pb2
from gcommon.v1.queue import consumer_pb2 as _consumer_pb2
from gcommon.v1.queue import consumer_group_config_pb2 as _consumer_group_config_pb2
from gcommon.v1.queue import consumer_group_stats_pb2 as _consumer_group_stats_pb2
from gcommon.v1.queue import group_coordinator_pb2 as _group_coordinator_pb2
from gcommon.v1.queue import partition_assignment_pb2 as _partition_assignment_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerGroup(_message.Message):
    __slots__ = ("group_id", "group_name", "topic", "config", "state", "consumers", "partition_assignments", "coordinator", "stats", "metadata", "created_at", "updated_at")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONSUMERS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    COORDINATOR_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    group_name: str
    topic: str
    config: _consumer_group_config_pb2.ConsumerGroupConfig
    state: _consumer_group_state_pb2.ConsumerGroupState
    consumers: _containers.RepeatedCompositeFieldContainer[_consumer_pb2.Consumer]
    partition_assignments: _containers.RepeatedCompositeFieldContainer[_partition_assignment_pb2.PartitionAssignment]
    coordinator: _group_coordinator_pb2.GroupCoordinator
    stats: _consumer_group_stats_pb2.ConsumerGroupStats
    metadata: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, group_id: _Optional[str] = ..., group_name: _Optional[str] = ..., topic: _Optional[str] = ..., config: _Optional[_Union[_consumer_group_config_pb2.ConsumerGroupConfig, _Mapping]] = ..., state: _Optional[_Union[_consumer_group_state_pb2.ConsumerGroupState, str]] = ..., consumers: _Optional[_Iterable[_Union[_consumer_pb2.Consumer, _Mapping]]] = ..., partition_assignments: _Optional[_Iterable[_Union[_partition_assignment_pb2.PartitionAssignment, _Mapping]]] = ..., coordinator: _Optional[_Union[_group_coordinator_pb2.GroupCoordinator, _Mapping]] = ..., stats: _Optional[_Union[_consumer_group_stats_pb2.ConsumerGroupStats, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
