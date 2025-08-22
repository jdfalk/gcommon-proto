from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BackupPolicy(_message.Message):
    __slots__ = ("enabled", "schedule", "retention_days", "location", "encrypted", "compressed", "verified", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    schedule: str
    retention_days: int
    location: str
    encrypted: bool
    compressed: bool
    verified: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., schedule: _Optional[str] = ..., retention_days: _Optional[int] = ..., location: _Optional[str] = ..., encrypted: bool = ..., compressed: bool = ..., verified: bool = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
