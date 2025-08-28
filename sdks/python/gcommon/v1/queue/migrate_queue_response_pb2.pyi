from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateQueueResponse(_message.Message):
    __slots__ = ("success", "new_queue_endpoint", "messages_migrated", "migration_duration_ms", "source_queue", "destination_queue", "error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    NEW_QUEUE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_MIGRATED_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_QUEUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    new_queue_endpoint: str
    messages_migrated: int
    migration_duration_ms: int
    source_queue: str
    destination_queue: str
    error: str
    def __init__(self, success: bool = ..., new_queue_endpoint: _Optional[str] = ..., messages_migrated: _Optional[int] = ..., migration_duration_ms: _Optional[int] = ..., source_queue: _Optional[str] = ..., destination_queue: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
