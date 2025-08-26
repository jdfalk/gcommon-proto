from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignRoleRequest(_message.Message):
    __slots__ = ("user_id", "role_id", "organization_id", "metadata", "assigned_by", "reason", "temporary", "expires_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_id: str
    organization_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    assigned_by: str
    reason: str
    temporary: bool
    expires_at: int
    def __init__(self, user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., assigned_by: _Optional[str] = ..., reason: _Optional[str] = ..., temporary: bool = ..., expires_at: _Optional[int] = ...) -> None: ...
