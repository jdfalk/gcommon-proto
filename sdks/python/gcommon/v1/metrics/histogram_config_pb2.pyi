from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramConfig(_message.Message):
    __slots__ = ("buckets", "auto_buckets", "max_buckets")
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    AUTO_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MAX_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedScalarFieldContainer[float]
    auto_buckets: bool
    max_buckets: int
    def __init__(self, buckets: _Optional[_Iterable[float]] = ..., auto_buckets: bool = ..., max_buckets: _Optional[int] = ...) -> None: ...
