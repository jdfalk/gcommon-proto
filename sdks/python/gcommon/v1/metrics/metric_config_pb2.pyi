from gcommon.v1.metrics import export_config_pb2 as _export_config_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricConfig(_message.Message):
    __slots__ = ("name", "metric_type", "enabled", "collection_interval", "retention_period", "default_labels", "description", "unit", "sampling_rate", "export_config")
    class DefaultLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    SAMPLING_RATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    metric_type: str
    enabled: bool
    collection_interval: _duration_pb2.Duration
    retention_period: _duration_pb2.Duration
    default_labels: _containers.ScalarMap[str, str]
    description: str
    unit: str
    sampling_rate: float
    export_config: _export_config_pb2.ExportConfig
    def __init__(self, name: _Optional[str] = ..., metric_type: _Optional[str] = ..., enabled: bool = ..., collection_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., default_labels: _Optional[_Mapping[str, str]] = ..., description: _Optional[str] = ..., unit: _Optional[str] = ..., sampling_rate: _Optional[float] = ..., export_config: _Optional[_Union[_export_config_pb2.ExportConfig, _Mapping]] = ...) -> None: ...
