from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.common import role_pb2 as _role_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListRolesResponse(_message.Message):
    __slots__ = ("roles", "pagination")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[_role_pb2.Role]
    pagination: _paginated_response_pb2.PaginatedResponse
    def __init__(self, roles: _Optional[_Iterable[_Union[_role_pb2.Role, _Mapping]]] = ..., pagination: _Optional[_Union[_paginated_response_pb2.PaginatedResponse, _Mapping]] = ...) -> None: ...
