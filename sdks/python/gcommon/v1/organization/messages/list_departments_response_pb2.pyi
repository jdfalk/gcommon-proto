from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.common.messages import paginated_response_pb2 as _paginated_response_pb2
from gcommon.v1.organization.messages import department_pb2 as _department_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListDepartmentsResponse(_message.Message):
    __slots__ = ("errors", "success", "departments", "pagination")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENTS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    departments: _containers.RepeatedCompositeFieldContainer[_department_pb2.Department]
    pagination: _paginated_response_pb2.PaginatedResponse
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: bool = ..., departments: _Optional[_Iterable[_Union[_department_pb2.Department, _Mapping]]] = ..., pagination: _Optional[_Union[_paginated_response_pb2.PaginatedResponse, _Mapping]] = ...) -> None: ...
