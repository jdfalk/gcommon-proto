from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreConfig(_message.Message):
    __slots__ = ("backup_source", "verify_integrity", "restore_strategy", "overwrite_existing", "timeout", "preserve_timestamps", "max_concurrency", "skip_corrupted")
    BACKUP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERIFY_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    RESTORE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    SKIP_CORRUPTED_FIELD_NUMBER: _ClassVar[int]
    backup_source: str
    verify_integrity: bool
    restore_strategy: str
    overwrite_existing: bool
    timeout: _duration_pb2.Duration
    preserve_timestamps: bool
    max_concurrency: int
    skip_corrupted: bool
    def __init__(self, backup_source: _Optional[str] = ..., verify_integrity: bool = ..., restore_strategy: _Optional[str] = ..., overwrite_existing: bool = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., preserve_timestamps: bool = ..., max_concurrency: _Optional[int] = ..., skip_corrupted: bool = ...) -> None: ...
