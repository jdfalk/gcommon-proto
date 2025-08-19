from gcommon.v1.queue.messages import size_bucket_pb2 as _size_bucket_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SizeDistribution(_message.Message):
    __slots__ = ("buckets", "min_size_bytes", "max_size_bytes", "average_size_bytes", "median_size_bytes")
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    MIN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[_size_bucket_pb2.SizeBucket]
    min_size_bytes: int
    max_size_bytes: int
    average_size_bytes: float
    median_size_bytes: float
    def __init__(self, buckets: _Optional[_Iterable[_Union[_size_bucket_pb2.SizeBucket, _Mapping]]] = ..., min_size_bytes: _Optional[int] = ..., max_size_bytes: _Optional[int] = ..., average_size_bytes: _Optional[float] = ..., median_size_bytes: _Optional[float] = ...) -> None: ...
