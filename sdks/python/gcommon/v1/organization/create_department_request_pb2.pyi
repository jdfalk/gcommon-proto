from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import department_pb2 as _department_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDepartmentRequest(_message.Message):
    __slots__ = ("metadata", "department", "validate_only")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    department: _department_pb2.Department
    validate_only: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., department: _Optional[_Union[_department_pb2.Department, _Mapping]] = ..., validate_only: _Optional[bool] = ...) -> None: ...
