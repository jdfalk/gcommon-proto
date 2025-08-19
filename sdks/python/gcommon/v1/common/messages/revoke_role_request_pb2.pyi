from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevokeRoleRequest(_message.Message):
    __slots__ = ("user_id", "role_id", "organization_id", "metadata", "revoked_by", "reason", "force")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_id: str
    organization_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    revoked_by: str
    reason: str
    force: bool
    def __init__(self, user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., organization_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., revoked_by: _Optional[str] = ..., reason: _Optional[str] = ..., force: bool = ...) -> None: ...
