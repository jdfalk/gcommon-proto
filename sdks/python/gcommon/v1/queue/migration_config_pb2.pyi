from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MigrationConfig(_message.Message):
    __slots__ = ("source_queue", "destination_queue", "migration_strategy", "batch_size", "timeout", "verify_integrity", "keep_source", "max_concurrency")
    SOURCE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_QUEUE_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    VERIFY_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    KEEP_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    source_queue: str
    destination_queue: str
    migration_strategy: str
    batch_size: int
    timeout: _duration_pb2.Duration
    verify_integrity: bool
    keep_source: bool
    max_concurrency: int
    def __init__(self, source_queue: _Optional[str] = ..., destination_queue: _Optional[str] = ..., migration_strategy: _Optional[str] = ..., batch_size: _Optional[int] = ..., timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., verify_integrity: bool = ..., keep_source: bool = ..., max_concurrency: _Optional[int] = ...) -> None: ...
