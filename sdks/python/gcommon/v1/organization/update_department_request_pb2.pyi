from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import department_pb2 as _department_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateDepartmentRequest(_message.Message):
    __slots__ = ("metadata", "department_id", "department", "update_mask", "validate_only")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    department_id: str
    department: _department_pb2.Department
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., department_id: _Optional[str] = ..., department: _Optional[_Union[_department_pb2.Department, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., validate_only: _Optional[bool] = ...) -> None: ...
