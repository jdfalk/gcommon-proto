from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BucketInfo(_message.Message):
    __slots__ = ("upper_bound", "count", "bucket_index")
    UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_INDEX_FIELD_NUMBER: _ClassVar[int]
    upper_bound: float
    count: int
    bucket_index: int
    def __init__(
        self,
        upper_bound: _Optional[float] = ...,
        count: _Optional[int] = ...,
        bucket_index: _Optional[int] = ...,
    ) -> None: ...
