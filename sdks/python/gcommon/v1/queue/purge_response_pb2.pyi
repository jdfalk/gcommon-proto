from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PurgeResponse(_message.Message):
    __slots__ = (
        "success",
        "messages_purged",
        "bytes_freed",
        "purge_duration_ms",
        "purged_partitions",
        "error",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_PURGED_FIELD_NUMBER: _ClassVar[int]
    BYTES_FREED_FIELD_NUMBER: _ClassVar[int]
    PURGE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    PURGED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    messages_purged: int
    bytes_freed: int
    purge_duration_ms: int
    purged_partitions: _containers.RepeatedScalarFieldContainer[int]
    error: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        messages_purged: _Optional[int] = ...,
        bytes_freed: _Optional[int] = ...,
        purge_duration_ms: _Optional[int] = ...,
        purged_partitions: _Optional[_Iterable[int]] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
