from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BackupQueueRequest(_message.Message):
    __slots__ = ("queue_name", "backup_path", "include_messages", "metadata_only", "format", "compression", "start_timestamp", "end_timestamp", "timeout_ms")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PATH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    backup_path: str
    include_messages: bool
    metadata_only: bool
    format: str
    compression: str
    start_timestamp: int
    end_timestamp: int
    timeout_ms: int
    def __init__(self, queue_name: _Optional[str] = ..., backup_path: _Optional[str] = ..., include_messages: _Optional[bool] = ..., metadata_only: _Optional[bool] = ..., format: _Optional[str] = ..., compression: _Optional[str] = ..., start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
