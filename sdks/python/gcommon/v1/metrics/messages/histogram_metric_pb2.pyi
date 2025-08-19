from gcommon.v1.metrics.messages import histogram_bucket_pb2 as _histogram_bucket_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistogramMetric(_message.Message):
    __slots__ = ("name", "labels", "buckets", "sample_count", "sample_sum", "timestamp", "help")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SUM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    name: str
    labels: _containers.ScalarMap[str, str]
    buckets: _containers.RepeatedCompositeFieldContainer[_histogram_bucket_pb2.HistogramBucket]
    sample_count: int
    sample_sum: float
    timestamp: _timestamp_pb2.Timestamp
    help: str
    def __init__(self, name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., buckets: _Optional[_Iterable[_Union[_histogram_bucket_pb2.HistogramBucket, _Mapping]]] = ..., sample_count: _Optional[int] = ..., sample_sum: _Optional[float] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., help: _Optional[str] = ...) -> None: ...
