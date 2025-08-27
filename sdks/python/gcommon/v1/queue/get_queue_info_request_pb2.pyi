from gcommon.v1.queue import time_range_filter_pb2 as _time_range_filter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueInfoRequest(_message.Message):
    __slots__ = (
        "queue_id",
        "include_stats",
        "include_config",
        "include_partitions",
        "include_consumer_groups",
        "include_subscriptions",
        "include_bindings",
        "include_errors",
        "time_range",
        "info_sections",
        "access_token",
    )
    QUEUE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CONSUMER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
    INFO_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    queue_id: str
    include_stats: bool
    include_config: bool
    include_partitions: bool
    include_consumer_groups: bool
    include_subscriptions: bool
    include_bindings: bool
    include_errors: bool
    time_range: _time_range_filter_pb2.TimeRangeFilter
    info_sections: _containers.RepeatedScalarFieldContainer[str]
    access_token: str
    def __init__(
        self,
        queue_id: _Optional[str] = ...,
        include_stats: _Optional[bool] = ...,
        include_config: _Optional[bool] = ...,
        include_partitions: _Optional[bool] = ...,
        include_consumer_groups: _Optional[bool] = ...,
        include_subscriptions: _Optional[bool] = ...,
        include_bindings: _Optional[bool] = ...,
        include_errors: _Optional[bool] = ...,
        time_range: _Optional[
            _Union[_time_range_filter_pb2.TimeRangeFilter, _Mapping]
        ] = ...,
        info_sections: _Optional[_Iterable[str]] = ...,
        access_token: _Optional[str] = ...,
    ) -> None: ...
