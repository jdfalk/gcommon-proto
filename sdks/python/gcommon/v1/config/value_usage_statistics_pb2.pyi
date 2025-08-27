import datetime

from gcommon.v1.config import value_usage_trend_pb2 as _value_usage_trend_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValueUsageStatistics(_message.Message):
    __slots__ = (
        "read_count",
        "write_count",
        "last_read_at",
        "last_written_at",
        "read_frequency",
        "write_frequency",
        "unique_readers",
        "unique_writers",
        "peak_usage_at",
        "peak_usage_count",
        "trends",
    )
    READ_COUNT_FIELD_NUMBER: _ClassVar[int]
    WRITE_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_WRITTEN_AT_FIELD_NUMBER: _ClassVar[int]
    READ_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    WRITE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_READERS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_WRITERS_FIELD_NUMBER: _ClassVar[int]
    PEAK_USAGE_AT_FIELD_NUMBER: _ClassVar[int]
    PEAK_USAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRENDS_FIELD_NUMBER: _ClassVar[int]
    read_count: int
    write_count: int
    last_read_at: _timestamp_pb2.Timestamp
    last_written_at: _timestamp_pb2.Timestamp
    read_frequency: float
    write_frequency: float
    unique_readers: int
    unique_writers: int
    peak_usage_at: _timestamp_pb2.Timestamp
    peak_usage_count: int
    trends: _containers.RepeatedCompositeFieldContainer[
        _value_usage_trend_pb2.ValueUsageTrend
    ]
    def __init__(
        self,
        read_count: _Optional[int] = ...,
        write_count: _Optional[int] = ...,
        last_read_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_written_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        read_frequency: _Optional[float] = ...,
        write_frequency: _Optional[float] = ...,
        unique_readers: _Optional[int] = ...,
        unique_writers: _Optional[int] = ...,
        peak_usage_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        peak_usage_count: _Optional[int] = ...,
        trends: _Optional[
            _Iterable[_Union[_value_usage_trend_pb2.ValueUsageTrend, _Mapping]]
        ] = ...,
    ) -> None: ...
