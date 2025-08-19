from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchingSettings(_message.Message):
    __slots__ = ("enabled", "batch_size", "timeout_minutes", "grouping_key")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MINUTES_FIELD_NUMBER: _ClassVar[int]
    GROUPING_KEY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    batch_size: int
    timeout_minutes: int
    grouping_key: str
    def __init__(self, enabled: bool = ..., batch_size: _Optional[int] = ..., timeout_minutes: _Optional[int] = ..., grouping_key: _Optional[str] = ...) -> None: ...
