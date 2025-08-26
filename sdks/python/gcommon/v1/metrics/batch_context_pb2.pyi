from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchContext(_message.Message):
    __slots__ = ("batch_id", "batch_position", "batch_size", "is_last")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_POSITION_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_LAST_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    batch_position: int
    batch_size: int
    is_last: bool
    def __init__(self, batch_id: _Optional[str] = ..., batch_position: _Optional[int] = ..., batch_size: _Optional[int] = ..., is_last: _Optional[bool] = ...) -> None: ...
