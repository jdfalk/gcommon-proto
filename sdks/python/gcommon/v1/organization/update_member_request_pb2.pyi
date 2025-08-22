from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import organization_member_pb2 as _organization_member_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMemberRequest(_message.Message):
    __slots__ = ("metadata", "member_id", "member", "update_mask")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    member_id: str
    member: _organization_member_pb2.OrganizationMember
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., member_id: _Optional[str] = ..., member: _Optional[_Union[_organization_member_pb2.OrganizationMember, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
