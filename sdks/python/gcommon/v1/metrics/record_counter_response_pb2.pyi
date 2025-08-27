import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import counter_metric_pb2 as _counter_metric_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordCounterResponse(_message.Message):
    __slots__ = ("success", "metric", "recorded_at", "error", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    RECORDED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    metric: _counter_metric_pb2.CounterMetric
    recorded_at: _timestamp_pb2.Timestamp
    error: _error_pb2.Error
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        success: _Optional[bool] = ...,
        metric: _Optional[_Union[_counter_metric_pb2.CounterMetric, _Mapping]] = ...,
        recorded_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
