import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsBackupInfo(_message.Message):
    __slots__ = ("backup_id", "backup_location", "backup_size_bytes", "backup_created_at", "backup_retention")
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_RETENTION_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    backup_location: str
    backup_size_bytes: int
    backup_created_at: _timestamp_pb2.Timestamp
    backup_retention: str
    def __init__(self, backup_id: _Optional[str] = ..., backup_location: _Optional[str] = ..., backup_size_bytes: _Optional[int] = ..., backup_created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., backup_retention: _Optional[str] = ...) -> None: ...
