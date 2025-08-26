from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PartitionConfig(_message.Message):
    __slots__ = ("partition_count", "partition_strategy", "partition_key", "custom_partition_function", "auto_scale", "min_partitions", "max_partitions", "scale_threshold_mb")
    PARTITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PARTITION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PARTITION_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCALE_FIELD_NUMBER: _ClassVar[int]
    MIN_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    SCALE_THRESHOLD_MB_FIELD_NUMBER: _ClassVar[int]
    partition_count: int
    partition_strategy: str
    partition_key: str
    custom_partition_function: str
    auto_scale: bool
    min_partitions: int
    max_partitions: int
    scale_threshold_mb: int
    def __init__(self, partition_count: _Optional[int] = ..., partition_strategy: _Optional[str] = ..., partition_key: _Optional[str] = ..., custom_partition_function: _Optional[str] = ..., auto_scale: bool = ..., min_partitions: _Optional[int] = ..., max_partitions: _Optional[int] = ..., scale_threshold_mb: _Optional[int] = ...) -> None: ...
