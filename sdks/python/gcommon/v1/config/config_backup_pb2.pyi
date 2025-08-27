import datetime

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigBackup(_message.Message):
    __slots__ = (
        "backup_id",
        "created_at",
        "config_values",
        "version",
        "environment",
        "created_by",
        "description",
        "backup_type",
        "checksum",
        "size_bytes",
        "compression",
        "storage_path",
        "retention_policy",
        "metadata",
    )
    class ConfigValuesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(
            self,
            key: _Optional[str] = ...,
            value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...,
        ) -> None: ...

    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    STORAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    RETENTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    created_at: _timestamp_pb2.Timestamp
    config_values: _containers.MessageMap[str, _any_pb2.Any]
    version: str
    environment: str
    created_by: str
    description: str
    backup_type: str
    checksum: str
    size_bytes: int
    compression: str
    storage_path: str
    retention_policy: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        backup_id: _Optional[str] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        config_values: _Optional[_Mapping[str, _any_pb2.Any]] = ...,
        version: _Optional[str] = ...,
        environment: _Optional[str] = ...,
        created_by: _Optional[str] = ...,
        description: _Optional[str] = ...,
        backup_type: _Optional[str] = ...,
        checksum: _Optional[str] = ...,
        size_bytes: _Optional[int] = ...,
        compression: _Optional[str] = ...,
        storage_path: _Optional[str] = ...,
        retention_policy: _Optional[str] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
