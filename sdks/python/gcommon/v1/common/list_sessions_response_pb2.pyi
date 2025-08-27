from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.common import session_pb2 as _session_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthListSessionsResponse(_message.Message):
    __slots__ = ("sessions", "pagination")
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[_session_pb2.Session]
    pagination: _paginated_response_pb2.PaginatedResponse
    def __init__(
        self,
        sessions: _Optional[_Iterable[_Union[_session_pb2.Session, _Mapping]]] = ...,
        pagination: _Optional[
            _Union[_paginated_response_pb2.PaginatedResponse, _Mapping]
        ] = ...,
    ) -> None: ...
