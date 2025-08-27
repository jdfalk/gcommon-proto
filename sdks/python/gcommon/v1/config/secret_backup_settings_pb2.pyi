import datetime

from gcommon.v1.common import (
    secret_backup_frequency_pb2 as _secret_backup_frequency_pb2,
)
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecretBackupSettings(_message.Message):
    __slots__ = (
        "enabled",
        "frequency",
        "retention_days",
        "storage_location",
        "encrypted",
        "compressed",
        "metadata",
        "last_backup_at",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LAST_BACKUP_AT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    frequency: _secret_backup_frequency_pb2.SecretBackupFrequency
    retention_days: int
    storage_location: str
    encrypted: bool
    compressed: bool
    metadata: _containers.ScalarMap[str, str]
    last_backup_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        frequency: _Optional[
            _Union[_secret_backup_frequency_pb2.SecretBackupFrequency, str]
        ] = ...,
        retention_days: _Optional[int] = ...,
        storage_location: _Optional[str] = ...,
        encrypted: _Optional[bool] = ...,
        compressed: _Optional[bool] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        last_backup_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
