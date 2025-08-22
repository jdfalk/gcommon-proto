from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordHistogramRequest(_message.Message):
    __slots__ = ("name", "value", "labels", "help", "unit", "buckets", "timestamp", "metadata", "sample_weight", "create_if_missing")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: float
    labels: _containers.ScalarMap[str, str]
    help: str
    unit: str
    buckets: _containers.RepeatedScalarFieldContainer[float]
    timestamp: _timestamp_pb2.Timestamp
    metadata: _request_metadata_pb2.RequestMetadata
    sample_weight: float
    create_if_missing: bool
    def __init__(self, name: _Optional[str] = ..., value: _Optional[float] = ..., labels: _Optional[_Mapping[str, str]] = ..., help: _Optional[str] = ..., unit: _Optional[str] = ..., buckets: _Optional[_Iterable[float]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., sample_weight: _Optional[float] = ..., create_if_missing: bool = ...) -> None: ...
