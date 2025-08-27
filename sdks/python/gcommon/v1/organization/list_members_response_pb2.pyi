from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.organization import organization_member_pb2 as _organization_member_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListMembersResponse(_message.Message):
    __slots__ = ("errors", "success", "members", "pagination")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    members: _containers.RepeatedCompositeFieldContainer[_organization_member_pb2.OrganizationMember]
    pagination: _paginated_response_pb2.PaginatedResponse
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: _Optional[bool] = ..., members: _Optional[_Iterable[_Union[_organization_member_pb2.OrganizationMember, _Mapping]]] = ..., pagination: _Optional[_Union[_paginated_response_pb2.PaginatedResponse, _Mapping]] = ...) -> None: ...
