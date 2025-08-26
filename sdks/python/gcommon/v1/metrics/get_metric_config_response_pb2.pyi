from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import metric_config_pb2 as _metric_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMetricConfigResponse(_message.Message):
    __slots__ = ("success", "error", "config")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    config: _metric_config_pb2.MetricConfig
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., config: _Optional[_Union[_metric_config_pb2.MetricConfig, _Mapping]] = ...) -> None: ...
