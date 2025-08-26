from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeletionStats(_message.Message):
    __slots__ = ("messages_deleted", "data_deleted_bytes", "subscriptions_deleted", "partitions_deleted", "deletion_duration_ms")
    MESSAGES_DELETED_FIELD_NUMBER: _ClassVar[int]
    DATA_DELETED_BYTES_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    DELETION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    messages_deleted: int
    data_deleted_bytes: int
    subscriptions_deleted: int
    partitions_deleted: int
    deletion_duration_ms: int
    def __init__(self, messages_deleted: _Optional[int] = ..., data_deleted_bytes: _Optional[int] = ..., subscriptions_deleted: _Optional[int] = ..., partitions_deleted: _Optional[int] = ..., deletion_duration_ms: _Optional[int] = ...) -> None: ...
