import datetime

from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import summary_quantile_pb2 as _summary_quantile_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SummaryMetric(_message.Message):
    __slots__ = ("name", "sample_count", "sample_sum", "quantiles", "labels", "timestamp", "help", "unit", "max_age", "metadata")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_SUM_FIELD_NUMBER: _ClassVar[int]
    QUANTILES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    sample_count: int
    sample_sum: float
    quantiles: _containers.RepeatedCompositeFieldContainer[_summary_quantile_pb2.SummaryQuantile]
    labels: _containers.ScalarMap[str, str]
    timestamp: _timestamp_pb2.Timestamp
    help: str
    unit: str
    max_age: _duration_pb2.Duration
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, name: _Optional[str] = ..., sample_count: _Optional[int] = ..., sample_sum: _Optional[float] = ..., quantiles: _Optional[_Iterable[_Union[_summary_quantile_pb2.SummaryQuantile, _Mapping]]] = ..., labels: _Optional[_Mapping[str, str]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., help: _Optional[str] = ..., unit: _Optional[str] = ..., max_age: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
