import datetime

from gcommon.v1.queue import backup_source_pb2 as _backup_source_pb2
from gcommon.v1.queue import restore_config_pb2 as _restore_config_pb2
from gcommon.v1.queue import restore_options_pb2 as _restore_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreQueueRequest(_message.Message):
    __slots__ = ("target_queue_id", "backup_source", "restore_config", "restore_point", "overwrite_existing", "validate_backup", "partition_ids", "options", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TARGET_QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESTORE_POINT_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    PARTITION_IDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    target_queue_id: str
    backup_source: _backup_source_pb2.BackupSource
    restore_config: _restore_config_pb2.RestoreConfig
    restore_point: _timestamp_pb2.Timestamp
    overwrite_existing: bool
    validate_backup: bool
    partition_ids: _containers.RepeatedScalarFieldContainer[int]
    options: _restore_options_pb2.RestoreOptions
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, target_queue_id: _Optional[str] = ..., backup_source: _Optional[_Union[_backup_source_pb2.BackupSource, _Mapping]] = ..., restore_config: _Optional[_Union[_restore_config_pb2.RestoreConfig, _Mapping]] = ..., restore_point: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., overwrite_existing: _Optional[bool] = ..., validate_backup: _Optional[bool] = ..., partition_ids: _Optional[_Iterable[int]] = ..., options: _Optional[_Union[_restore_options_pb2.RestoreOptions, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
