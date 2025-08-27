from gcommon.v1.metrics import metric_config_pb2 as _metric_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMetricConfigRequest(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _metric_config_pb2.MetricConfig
    def __init__(
        self, config: _Optional[_Union[_metric_config_pb2.MetricConfig, _Mapping]] = ...
    ) -> None: ...
