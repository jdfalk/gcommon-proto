import datetime

from gcommon.v1.metrics import (
    export_destination_stats_pb2 as _export_destination_stats_pb2,
)
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportStats(_message.Message):
    __slots__ = (
        "total_exported_metrics",
        "total_exported_data_points",
        "export_rate_metrics_per_second",
        "failed_exports",
        "export_success_rate",
        "export_destinations",
        "last_successful_export",
    )
    TOTAL_EXPORTED_METRICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EXPORTED_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RATE_METRICS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_SUCCESSFUL_EXPORT_FIELD_NUMBER: _ClassVar[int]
    total_exported_metrics: int
    total_exported_data_points: int
    export_rate_metrics_per_second: float
    failed_exports: int
    export_success_rate: float
    export_destinations: _containers.RepeatedCompositeFieldContainer[
        _export_destination_stats_pb2.ExportDestinationStats
    ]
    last_successful_export: _timestamp_pb2.Timestamp
    def __init__(
        self,
        total_exported_metrics: _Optional[int] = ...,
        total_exported_data_points: _Optional[int] = ...,
        export_rate_metrics_per_second: _Optional[float] = ...,
        failed_exports: _Optional[int] = ...,
        export_success_rate: _Optional[float] = ...,
        export_destinations: _Optional[
            _Iterable[
                _Union[_export_destination_stats_pb2.ExportDestinationStats, _Mapping]
            ]
        ] = ...,
        last_successful_export: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
