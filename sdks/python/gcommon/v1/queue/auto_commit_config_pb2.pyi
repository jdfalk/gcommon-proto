from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AutoCommitConfig(_message.Message):
    __slots__ = ("enabled", "interval_ms", "commit_on_completion", "batch_size")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ON_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    interval_ms: int
    commit_on_completion: bool
    batch_size: int
    def __init__(self, enabled: _Optional[bool] = ..., interval_ms: _Optional[int] = ..., commit_on_completion: _Optional[bool] = ..., batch_size: _Optional[int] = ...) -> None: ...
