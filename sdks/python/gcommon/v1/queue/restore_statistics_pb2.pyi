from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreStatistics(_message.Message):
    __slots__ = ("messages_restored", "bytes_restored", "partitions_restored", "messages_skipped", "messages_failed", "restore_rate", "throughput_bps", "backup_size_bytes", "compression_ratio")
    MESSAGES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_RESTORED_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FAILED_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RATE_FIELD_NUMBER: _ClassVar[int]
    THROUGHPUT_BPS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_RATIO_FIELD_NUMBER: _ClassVar[int]
    messages_restored: int
    bytes_restored: int
    partitions_restored: int
    messages_skipped: int
    messages_failed: int
    restore_rate: float
    throughput_bps: float
    backup_size_bytes: int
    compression_ratio: float
    def __init__(self, messages_restored: _Optional[int] = ..., bytes_restored: _Optional[int] = ..., partitions_restored: _Optional[int] = ..., messages_skipped: _Optional[int] = ..., messages_failed: _Optional[int] = ..., restore_rate: _Optional[float] = ..., throughput_bps: _Optional[float] = ..., backup_size_bytes: _Optional[int] = ..., compression_ratio: _Optional[float] = ...) -> None: ...
