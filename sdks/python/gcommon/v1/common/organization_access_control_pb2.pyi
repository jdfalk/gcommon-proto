from gcommon.v1.common import time_restriction_pb2 as _time_restriction_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationAccessControl(_message.Message):
    __slots__ = ("ip_whitelist", "auth_methods", "session_timeout", "max_concurrent_sessions", "allowed_countries", "time_restrictions")
    IP_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHODS_FIELD_NUMBER: _ClassVar[int]
    SESSION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    TIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    ip_whitelist: _containers.RepeatedScalarFieldContainer[str]
    auth_methods: _containers.RepeatedScalarFieldContainer[str]
    session_timeout: int
    max_concurrent_sessions: int
    allowed_countries: _containers.RepeatedScalarFieldContainer[str]
    time_restrictions: _containers.RepeatedCompositeFieldContainer[_time_restriction_pb2.TimeRestriction]
    def __init__(self, ip_whitelist: _Optional[_Iterable[str]] = ..., auth_methods: _Optional[_Iterable[str]] = ..., session_timeout: _Optional[int] = ..., max_concurrent_sessions: _Optional[int] = ..., allowed_countries: _Optional[_Iterable[str]] = ..., time_restrictions: _Optional[_Iterable[_Union[_time_restriction_pb2.TimeRestriction, _Mapping]]] = ...) -> None: ...
