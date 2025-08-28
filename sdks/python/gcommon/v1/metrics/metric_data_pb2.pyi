from gcommon.v1.common import metric_type_pb2 as _metric_type_pb2
from gcommon.v1.metrics import metric_value_pb2 as _metric_value_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricData(_message.Message):
    __slots__ = ("metric_id", "name", "type", "description", "unit", "labels", "values", "created_at", "source", "namespace", "schema_version")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_VERSION_FIELD_NUMBER: _ClassVar[int]
    metric_id: str
    name: str
    type: _metric_type_pb2.MetricsMetricType
    description: str
    unit: str
    labels: _containers.ScalarMap[str, str]
    values: _containers.RepeatedCompositeFieldContainer[_metric_value_pb2.MetricValue]
    created_at: _timestamp_pb2.Timestamp
    source: str
    namespace: str
    schema_version: str
    def __init__(self, metric_id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[_metric_type_pb2.MetricsMetricType, str]] = ..., description: _Optional[str] = ..., unit: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., values: _Optional[_Iterable[_Union[_metric_value_pb2.MetricValue, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source: _Optional[str] = ..., namespace: _Optional[str] = ..., schema_version: _Optional[str] = ...) -> None: ...
