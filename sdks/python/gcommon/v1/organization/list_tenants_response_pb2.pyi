from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.organization import tenant_pb2 as _tenant_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListTenantsResponse(_message.Message):
    __slots__ = ("errors", "success", "tenants", "pagination")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    tenants: _containers.RepeatedCompositeFieldContainer[_tenant_pb2.Tenant]
    pagination: _paginated_response_pb2.PaginatedResponse
    def __init__(
        self,
        errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ...,
        success: _Optional[bool] = ...,
        tenants: _Optional[_Iterable[_Union[_tenant_pb2.Tenant, _Mapping]]] = ...,
        pagination: _Optional[
            _Union[_paginated_response_pb2.PaginatedResponse, _Mapping]
        ] = ...,
    ) -> None: ...
