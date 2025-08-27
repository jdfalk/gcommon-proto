import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import session_info_pb2 as _session_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListUserSessionsResponse(_message.Message):
    __slots__ = (
        "sessions",
        "total_count",
        "pagination",
        "request_metadata",
        "includes_current_session",
        "active_session_count",
        "user_id",
        "error",
        "generated_at",
        "data_refreshed_at",
    )
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDES_CURRENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    DATA_REFRESHED_AT_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_info_pb2.SessionInfo]
    total_count: int
    pagination: _paginated_response_pb2.PaginatedResponse
    request_metadata: _request_metadata_pb2.RequestMetadata
    includes_current_session: bool
    active_session_count: int
    user_id: str
    error: _error_pb2.Error
    generated_at: _timestamp_pb2.Timestamp
    data_refreshed_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        sessions: _Optional[
            _Iterable[_Union[_session_info_pb2.SessionInfo, _Mapping]]
        ] = ...,
        total_count: _Optional[int] = ...,
        pagination: _Optional[
            _Union[_paginated_response_pb2.PaginatedResponse, _Mapping]
        ] = ...,
        request_metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        includes_current_session: _Optional[bool] = ...,
        active_session_count: _Optional[int] = ...,
        user_id: _Optional[str] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
        generated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        data_refreshed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
