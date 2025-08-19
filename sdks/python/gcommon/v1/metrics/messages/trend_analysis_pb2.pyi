from gcommon.v1.metrics.messages import data_volume_trend_pb2 as _data_volume_trend_pb2
from gcommon.v1.metrics.messages import error_trend_pb2 as _error_trend_pb2
from gcommon.v1.metrics.messages import performance_trend_pb2 as _performance_trend_pb2
from gcommon.v1.metrics.messages import resource_usage_trend_pb2 as _resource_usage_trend_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrendAnalysis(_message.Message):
    __slots__ = ("performance", "resource_usage", "errors", "data_volume")
    PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    DATA_VOLUME_FIELD_NUMBER: _ClassVar[int]
    performance: _performance_trend_pb2.PerformanceTrend
    resource_usage: _resource_usage_trend_pb2.ResourceUsageTrend
    errors: _error_trend_pb2.ErrorTrend
    data_volume: _data_volume_trend_pb2.DataVolumeTrend
    def __init__(self, performance: _Optional[_Union[_performance_trend_pb2.PerformanceTrend, _Mapping]] = ..., resource_usage: _Optional[_Union[_resource_usage_trend_pb2.ResourceUsageTrend, _Mapping]] = ..., errors: _Optional[_Union[_error_trend_pb2.ErrorTrend, _Mapping]] = ..., data_volume: _Optional[_Union[_data_volume_trend_pb2.DataVolumeTrend, _Mapping]] = ...) -> None: ...
