from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumerConfig(_message.Message):
    __slots__ = (
        "timeout_ms",
        "max_poll_records",
        "fetch_min_bytes",
        "fetch_max_wait_ms",
        "auto_offset_reset",
        "priority",
    )
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_POLL_RECORDS_FIELD_NUMBER: _ClassVar[int]
    FETCH_MIN_BYTES_FIELD_NUMBER: _ClassVar[int]
    FETCH_MAX_WAIT_MS_FIELD_NUMBER: _ClassVar[int]
    AUTO_OFFSET_RESET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    timeout_ms: int
    max_poll_records: int
    fetch_min_bytes: int
    fetch_max_wait_ms: int
    auto_offset_reset: bool
    priority: int
    def __init__(
        self,
        timeout_ms: _Optional[int] = ...,
        max_poll_records: _Optional[int] = ...,
        fetch_min_bytes: _Optional[int] = ...,
        fetch_max_wait_ms: _Optional[int] = ...,
        auto_offset_reset: _Optional[bool] = ...,
        priority: _Optional[int] = ...,
    ) -> None: ...
