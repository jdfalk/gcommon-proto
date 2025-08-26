from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterInfo(_message.Message):
    __slots__ = ("cluster_id", "name", "version", "node_count", "active_brokers", "status", "uptime_seconds", "total_topics", "total_partitions", "leader_node", "metadata", "last_health_check")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_BROKERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPTIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOPICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    LEADER_NODE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LAST_HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    name: str
    version: str
    node_count: int
    active_brokers: int
    status: str
    uptime_seconds: int
    total_topics: int
    total_partitions: int
    leader_node: str
    metadata: _containers.ScalarMap[str, str]
    last_health_check: _timestamp_pb2.Timestamp
    def __init__(self, cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., node_count: _Optional[int] = ..., active_brokers: _Optional[int] = ..., status: _Optional[str] = ..., uptime_seconds: _Optional[int] = ..., total_topics: _Optional[int] = ..., total_partitions: _Optional[int] = ..., leader_node: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., last_health_check: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
