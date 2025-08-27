from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DryRunResult(_message.Message):
    __slots__ = (
        "would_delete_bytes",
        "would_delete_points",
        "would_delete_indices",
        "would_stop_exports",
        "estimated_deletion_time",
    )
    WOULD_DELETE_BYTES_FIELD_NUMBER: _ClassVar[int]
    WOULD_DELETE_POINTS_FIELD_NUMBER: _ClassVar[int]
    WOULD_DELETE_INDICES_FIELD_NUMBER: _ClassVar[int]
    WOULD_STOP_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DELETION_TIME_FIELD_NUMBER: _ClassVar[int]
    would_delete_bytes: int
    would_delete_points: int
    would_delete_indices: int
    would_stop_exports: int
    estimated_deletion_time: str
    def __init__(
        self,
        would_delete_bytes: _Optional[int] = ...,
        would_delete_points: _Optional[int] = ...,
        would_delete_indices: _Optional[int] = ...,
        would_stop_exports: _Optional[int] = ...,
        estimated_deletion_time: _Optional[str] = ...,
    ) -> None: ...
