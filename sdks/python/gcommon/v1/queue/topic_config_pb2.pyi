from gcommon.v1.queue import partition_config_pb2 as _partition_config_pb2
from gcommon.v1.queue import retention_policy_pb2 as _retention_policy_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TopicConfig(_message.Message):
    __slots__ = ("max_messages", "max_size_bytes", "retention_policy", "partition_config", "persistent", "replicated", "replication_factor", "enable_compaction")
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    REPLICATED_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPACTION_FIELD_NUMBER: _ClassVar[int]
    max_messages: int
    max_size_bytes: int
    retention_policy: _retention_policy_pb2.QueueRetentionPolicy
    partition_config: _partition_config_pb2.PartitionConfig
    persistent: bool
    replicated: bool
    replication_factor: int
    enable_compaction: bool
    def __init__(self, max_messages: _Optional[int] = ..., max_size_bytes: _Optional[int] = ..., retention_policy: _Optional[_Union[_retention_policy_pb2.QueueRetentionPolicy, _Mapping]] = ..., partition_config: _Optional[_Union[_partition_config_pb2.PartitionConfig, _Mapping]] = ..., persistent: _Optional[bool] = ..., replicated: _Optional[bool] = ..., replication_factor: _Optional[int] = ..., enable_compaction: _Optional[bool] = ...) -> None: ...
