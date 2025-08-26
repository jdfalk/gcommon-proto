from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.organization import department_pb2 as _department_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDepartmentResponse(_message.Message):
    __slots__ = ("errors", "success", "department")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    department: _department_pb2.Department
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: _Optional[bool] = ..., department: _Optional[_Union[_department_pb2.Department, _Mapping]] = ...) -> None: ...
