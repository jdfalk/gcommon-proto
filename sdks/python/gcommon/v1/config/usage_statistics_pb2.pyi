import datetime

from gcommon.v1.config import usage_trend_pb2 as _usage_trend_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UsageStatistics(_message.Message):
    __slots__ = (
        "total_access_count",
        "access_count_24h",
        "access_count_7d",
        "access_count_30d",
        "unique_users_count",
        "unique_services_count",
        "avg_access_frequency",
        "peak_access_at",
        "peak_access_count",
        "trends",
    )
    TOTAL_ACCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_COUNT_24H_FIELD_NUMBER: _ClassVar[int]
    ACCESS_COUNT_7D_FIELD_NUMBER: _ClassVar[int]
    ACCESS_COUNT_30D_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_USERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_SERVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVG_ACCESS_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PEAK_ACCESS_AT_FIELD_NUMBER: _ClassVar[int]
    PEAK_ACCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRENDS_FIELD_NUMBER: _ClassVar[int]
    total_access_count: int
    access_count_24h: int
    access_count_7d: int
    access_count_30d: int
    unique_users_count: int
    unique_services_count: int
    avg_access_frequency: float
    peak_access_at: _timestamp_pb2.Timestamp
    peak_access_count: int
    trends: _containers.RepeatedCompositeFieldContainer[_usage_trend_pb2.UsageTrend]
    def __init__(
        self,
        total_access_count: _Optional[int] = ...,
        access_count_24h: _Optional[int] = ...,
        access_count_7d: _Optional[int] = ...,
        access_count_30d: _Optional[int] = ...,
        unique_users_count: _Optional[int] = ...,
        unique_services_count: _Optional[int] = ...,
        avg_access_frequency: _Optional[float] = ...,
        peak_access_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        peak_access_count: _Optional[int] = ...,
        trends: _Optional[
            _Iterable[_Union[_usage_trend_pb2.UsageTrend, _Mapping]]
        ] = ...,
    ) -> None: ...
