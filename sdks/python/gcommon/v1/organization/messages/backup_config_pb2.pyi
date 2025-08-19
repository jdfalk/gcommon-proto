from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationBackupConfig(_message.Message):
    __slots__ = ("enabled", "frequency", "retention_days", "storage_location", "point_in_time_recovery")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    POINT_IN_TIME_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    frequency: str
    retention_days: int
    storage_location: str
    point_in_time_recovery: bool
    def __init__(self, enabled: bool = ..., frequency: _Optional[str] = ..., retention_days: _Optional[int] = ..., storage_location: _Optional[str] = ..., point_in_time_recovery: bool = ...) -> None: ...
