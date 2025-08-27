import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurgeOptions(_message.Message):
    __slots__ = (
        "purge_all",
        "older_than",
        "header_filters",
        "priority_below",
        "priority_above",
        "max_messages",
        "only_failed",
        "only_expired",
    )
    class HeaderFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    PURGE_ALL_FIELD_NUMBER: _ClassVar[int]
    OLDER_THAN_FIELD_NUMBER: _ClassVar[int]
    HEADER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_BELOW_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_ABOVE_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ONLY_FAILED_FIELD_NUMBER: _ClassVar[int]
    ONLY_EXPIRED_FIELD_NUMBER: _ClassVar[int]
    purge_all: bool
    older_than: _timestamp_pb2.Timestamp
    header_filters: _containers.ScalarMap[str, str]
    priority_below: int
    priority_above: int
    max_messages: int
    only_failed: bool
    only_expired: bool
    def __init__(
        self,
        purge_all: _Optional[bool] = ...,
        older_than: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        header_filters: _Optional[_Mapping[str, str]] = ...,
        priority_below: _Optional[int] = ...,
        priority_above: _Optional[int] = ...,
        max_messages: _Optional[int] = ...,
        only_failed: _Optional[bool] = ...,
        only_expired: _Optional[bool] = ...,
    ) -> None: ...
