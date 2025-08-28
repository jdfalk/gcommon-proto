from gcommon.v1.common import metric_type_pb2 as _metric_type_pb2
from gcommon.v1.common import metrics_retention_policy_config_pb2 as _metrics_retention_policy_config_pb2
from gcommon.v1.metrics import export_config_pb2 as _export_config_pb2
from gcommon.v1.metrics import label_definition_pb2 as _label_definition_pb2
from gcommon.v1.metrics import metric_type_config_pb2 as _metric_type_config_pb2
from gcommon.v1.metrics import validation_rules_pb2 as _validation_rules_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricDefinition(_message.Message):
    __slots__ = ("name", "type", "description", "unit", "labels", "config", "retention", "export_config", "validation", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _metric_type_pb2.MetricsMetricType
    description: str
    unit: str
    labels: _containers.RepeatedCompositeFieldContainer[_label_definition_pb2.LabelDefinition]
    config: _metric_type_config_pb2.MetricTypeConfig
    retention: _metrics_retention_policy_config_pb2.MetricsRetentionPolicyConfig
    export_config: _export_config_pb2.ExportConfig
    validation: _validation_rules_pb2.ValidationRules
    tags: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_metric_type_pb2.MetricsMetricType, str]] = ..., description: _Optional[str] = ..., unit: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_label_definition_pb2.LabelDefinition, _Mapping]]] = ..., config: _Optional[_Union[_metric_type_config_pb2.MetricTypeConfig, _Mapping]] = ..., retention: _Optional[_Union[_metrics_retention_policy_config_pb2.MetricsRetentionPolicyConfig, _Mapping]] = ..., export_config: _Optional[_Union[_export_config_pb2.ExportConfig, _Mapping]] = ..., validation: _Optional[_Union[_validation_rules_pb2.ValidationRules, _Mapping]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
