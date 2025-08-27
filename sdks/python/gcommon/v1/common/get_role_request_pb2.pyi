from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRoleRequest(_message.Message):
    __slots__ = ("role_id", "include_permissions", "metadata")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    include_permissions: bool
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, role_id: _Optional[str] = ..., include_permissions: _Optional[bool] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
