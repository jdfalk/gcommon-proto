from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchSettings(_message.Message):
    __slots__ = ("enabled", "max_batch_size", "max_batch_bytes", "batch_timeout_ms", "flush_on_complete")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_BATCH_BYTES_FIELD_NUMBER: _ClassVar[int]
    BATCH_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    FLUSH_ON_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    max_batch_size: int
    max_batch_bytes: int
    batch_timeout_ms: int
    flush_on_complete: bool
    def __init__(self, enabled: _Optional[bool] = ..., max_batch_size: _Optional[int] = ..., max_batch_bytes: _Optional[int] = ..., batch_timeout_ms: _Optional[int] = ..., flush_on_complete: _Optional[bool] = ...) -> None: ...
