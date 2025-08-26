from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MigrateQueueRequest(_message.Message):
    __slots__ = ("source_queue", "destination_queue", "destination_endpoint", "preserve_order", "verify_integrity", "max_duration_ms", "batch_size", "timeout_ms")
    SOURCE_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_QUEUE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_ORDER_FIELD_NUMBER: _ClassVar[int]
    VERIFY_INTEGRITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    source_queue: str
    destination_queue: str
    destination_endpoint: str
    preserve_order: bool
    verify_integrity: bool
    max_duration_ms: int
    batch_size: int
    timeout_ms: int
    def __init__(self, source_queue: _Optional[str] = ..., destination_queue: _Optional[str] = ..., destination_endpoint: _Optional[str] = ..., preserve_order: _Optional[bool] = ..., verify_integrity: _Optional[bool] = ..., max_duration_ms: _Optional[int] = ..., batch_size: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
