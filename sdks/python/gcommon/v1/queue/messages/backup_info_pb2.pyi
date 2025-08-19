from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueBackupInfo(_message.Message):
    __slots__ = ("backup_id", "backup_location", "backup_size_bytes", "backup_created_at", "backup_expires_at")
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUP_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    BACKUP_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    backup_location: str
    backup_size_bytes: int
    backup_created_at: _timestamp_pb2.Timestamp
    backup_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, backup_id: _Optional[str] = ..., backup_location: _Optional[str] = ..., backup_size_bytes: _Optional[int] = ..., backup_created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., backup_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
