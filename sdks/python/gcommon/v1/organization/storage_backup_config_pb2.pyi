from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StorageBackupConfig(_message.Message):
    __slots__ = ("enabled", "schedule", "retention_days", "cross_region", "encryption_enabled")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    CROSS_REGION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    schedule: str
    retention_days: int
    cross_region: bool
    encryption_enabled: bool
    def __init__(self, enabled: bool = ..., schedule: _Optional[str] = ..., retention_days: _Optional[int] = ..., cross_region: bool = ..., encryption_enabled: bool = ...) -> None: ...
