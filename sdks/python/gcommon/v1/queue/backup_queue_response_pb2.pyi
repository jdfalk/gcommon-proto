from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BackupQueueResponse(_message.Message):
    __slots__ = ("success", "backup_location", "messages_backed_up", "backup_size_bytes", "backup_duration_ms", "checksum", "backup_timestamp", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_BACKED_UP_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    backup_location: str
    messages_backed_up: int
    backup_size_bytes: int
    backup_duration_ms: int
    checksum: str
    backup_timestamp: int
    error: str
    def __init__(self, success: _Optional[bool] = ..., backup_location: _Optional[str] = ..., messages_backed_up: _Optional[int] = ..., backup_size_bytes: _Optional[int] = ..., backup_duration_ms: _Optional[int] = ..., checksum: _Optional[str] = ..., backup_timestamp: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
