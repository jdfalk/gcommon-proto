from gcommon.v1.queue.messages import historical_data_point_pb2 as _historical_data_point_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistoricalStats(_message.Message):
    __slots__ = ("data_points", "aggregation_period")
    DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    data_points: _containers.RepeatedCompositeFieldContainer[_historical_data_point_pb2.HistoricalDataPoint]
    aggregation_period: _duration_pb2.Duration
    def __init__(self, data_points: _Optional[_Iterable[_Union[_historical_data_point_pb2.HistoricalDataPoint, _Mapping]]] = ..., aggregation_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
