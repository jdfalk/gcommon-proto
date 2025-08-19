from gcommon.v1.metrics.messages import counter_config_pb2 as _counter_config_pb2
from gcommon.v1.metrics.messages import gauge_config_pb2 as _gauge_config_pb2
from gcommon.v1.metrics.messages import histogram_config_pb2 as _histogram_config_pb2
from gcommon.v1.metrics.messages import summary_config_pb2 as _summary_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricTypeConfig(_message.Message):
    __slots__ = ("histogram", "summary", "gauge", "counter")
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    GAUGE_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    histogram: _histogram_config_pb2.HistogramConfig
    summary: _summary_config_pb2.SummaryConfig
    gauge: _gauge_config_pb2.GaugeConfig
    counter: _counter_config_pb2.CounterConfig
    def __init__(self, histogram: _Optional[_Union[_histogram_config_pb2.HistogramConfig, _Mapping]] = ..., summary: _Optional[_Union[_summary_config_pb2.SummaryConfig, _Mapping]] = ..., gauge: _Optional[_Union[_gauge_config_pb2.GaugeConfig, _Mapping]] = ..., counter: _Optional[_Union[_counter_config_pb2.CounterConfig, _Mapping]] = ...) -> None: ...
