from gcommon.v1.metrics.messages import retention_info_pb2 as _retention_info_pb2
from gcommon.v1.queue.messages import owner_info_pb2 as _owner_info_pb2
from gcommon.v1.queue.messages import partition_info_pb2 as _partition_info_pb2
from gcommon.v1.queue.messages import topic_configuration_pb2 as _topic_configuration_pb2
from gcommon.v1.queue.messages import topic_permissions_pb2 as _topic_permissions_pb2
from gcommon.v1.queue.messages import topic_stats_pb2 as _topic_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTopicInfoResponse(_message.Message):
    __slots__ = ("topic_id", "topic_name", "description", "created_at", "updated_at", "stats", "partitions", "config", "state", "permissions", "metadata", "tags", "owner", "retention")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    topic_name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    stats: _topic_stats_pb2.TopicStats
    partitions: _containers.RepeatedCompositeFieldContainer[_partition_info_pb2.PartitionInfo]
    config: _topic_configuration_pb2.TopicConfiguration
    state: str
    permissions: _topic_permissions_pb2.TopicPermissions
    metadata: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    owner: _owner_info_pb2.OwnerInfo
    retention: _retention_info_pb2.MetricsRetentionInfo
    def __init__(self, topic_id: _Optional[str] = ..., topic_name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stats: _Optional[_Union[_topic_stats_pb2.TopicStats, _Mapping]] = ..., partitions: _Optional[_Iterable[_Union[_partition_info_pb2.PartitionInfo, _Mapping]]] = ..., config: _Optional[_Union[_topic_configuration_pb2.TopicConfiguration, _Mapping]] = ..., state: _Optional[str] = ..., permissions: _Optional[_Union[_topic_permissions_pb2.TopicPermissions, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Iterable[str]] = ..., owner: _Optional[_Union[_owner_info_pb2.OwnerInfo, _Mapping]] = ..., retention: _Optional[_Union[_retention_info_pb2.MetricsRetentionInfo, _Mapping]] = ...) -> None: ...
