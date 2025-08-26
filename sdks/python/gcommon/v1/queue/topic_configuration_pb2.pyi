from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TopicConfiguration(_message.Message):
    __slots__ = ("partition_count", "replication_factor", "retention_period_seconds", "max_message_size_bytes", "compression_enabled", "compression_algorithm", "encryption_enabled", "cleanup_policy", "min_insync_replicas", "segment_size_bytes")
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    MIN_INSYNC_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    partition_count: int
    replication_factor: int
    retention_period_seconds: int
    max_message_size_bytes: int
    compression_enabled: bool
    compression_algorithm: str
    encryption_enabled: bool
    cleanup_policy: str
    min_insync_replicas: int
    segment_size_bytes: int
    def __init__(self, partition_count: _Optional[int] = ..., replication_factor: _Optional[int] = ..., retention_period_seconds: _Optional[int] = ..., max_message_size_bytes: _Optional[int] = ..., compression_enabled: _Optional[bool] = ..., compression_algorithm: _Optional[str] = ..., encryption_enabled: _Optional[bool] = ..., cleanup_policy: _Optional[str] = ..., min_insync_replicas: _Optional[int] = ..., segment_size_bytes: _Optional[int] = ...) -> None: ...
