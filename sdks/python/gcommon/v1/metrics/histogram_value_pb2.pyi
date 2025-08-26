from gcommon.v1.metrics import histogram_bucket_pb2 as _histogram_bucket_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramValue(_message.Message):
    __slots__ = ("buckets", "count", "sum")
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[_histogram_bucket_pb2.HistogramBucket]
    count: int
    sum: float
    def __init__(self, buckets: _Optional[_Iterable[_Union[_histogram_bucket_pb2.HistogramBucket, _Mapping]]] = ..., count: _Optional[int] = ..., sum: _Optional[float] = ...) -> None: ...
