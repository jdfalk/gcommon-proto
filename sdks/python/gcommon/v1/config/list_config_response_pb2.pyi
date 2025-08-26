from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.config import config_entry_pb2 as _config_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListConfigResponse(_message.Message):
    __slots__ = ("entries", "pagination", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_config_entry_pb2.ConfigEntry]
    pagination: _paginated_response_pb2.PaginatedResponse
    error: _error_pb2.Error
    def __init__(self, entries: _Optional[_Iterable[_Union[_config_entry_pb2.ConfigEntry, _Mapping]]] = ..., pagination: _Optional[_Union[_paginated_response_pb2.PaginatedResponse, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
