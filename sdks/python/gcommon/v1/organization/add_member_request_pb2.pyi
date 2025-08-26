from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import organization_member_pb2 as _organization_member_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddMemberRequest(_message.Message):
    __slots__ = ("metadata", "organization_id", "member", "send_invite")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    SEND_INVITE_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    organization_id: str
    member: _organization_member_pb2.OrganizationMember
    send_invite: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., organization_id: _Optional[str] = ..., member: _Optional[_Union[_organization_member_pb2.OrganizationMember, _Mapping]] = ..., send_invite: _Optional[bool] = ...) -> None: ...
