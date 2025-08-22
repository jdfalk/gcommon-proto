from gcommon.v1.config import backup_frequency_pb2 as _backup_frequency_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupSettings(_message.Message):
    __slots__ = ("enabled", "frequency", "retention_days", "storage_location", "encrypted", "compressed", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    frequency: _backup_frequency_pb2.BackupFrequency
    retention_days: int
    storage_location: str
    encrypted: bool
    compressed: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., frequency: _Optional[_Union[_backup_frequency_pb2.BackupFrequency, str]] = ..., retention_days: _Optional[int] = ..., storage_location: _Optional[str] = ..., encrypted: bool = ..., compressed: bool = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
