from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import role_pb2 as _role_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateRoleRequest(_message.Message):
    __slots__ = ("role", "update_mask", "metadata")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    update_mask: _field_mask_pb2.FieldMask
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
