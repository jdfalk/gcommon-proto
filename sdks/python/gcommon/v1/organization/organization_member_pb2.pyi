import datetime

from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.common import member_role_pb2 as _member_role_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationMember(_message.Message):
    __slots__ = (
        "id",
        "organization_id",
        "user_id",
        "email",
        "display_name",
        "role",
        "additional_roles",
        "permissions",
        "department_ids",
        "team_ids",
        "tenant_ids",
        "metadata",
        "created_at",
        "updated_at",
        "last_active_at",
        "invited_by",
        "updated_by",
        "active",
        "job_title",
        "manager_id",
        "direct_report_ids",
        "avatar_url",
        "phone",
        "location",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ROLES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    TEAM_IDS_FIELD_NUMBER: _ClassVar[int]
    TENANT_IDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    INVITED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    JOB_TITLE_FIELD_NUMBER: _ClassVar[int]
    MANAGER_ID_FIELD_NUMBER: _ClassVar[int]
    DIRECT_REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    user_id: str
    email: str
    display_name: str
    role: _member_role_pb2.MemberRole
    additional_roles: _containers.RepeatedScalarFieldContainer[
        _member_role_pb2.MemberRole
    ]
    permissions: _containers.RepeatedScalarFieldContainer[str]
    department_ids: _containers.RepeatedScalarFieldContainer[str]
    team_ids: _containers.RepeatedScalarFieldContainer[str]
    tenant_ids: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_active_at: _timestamp_pb2.Timestamp
    invited_by: str
    updated_by: str
    active: bool
    job_title: str
    manager_id: str
    direct_report_ids: _containers.RepeatedScalarFieldContainer[str]
    avatar_url: str
    phone: str
    location: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        organization_id: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        email: _Optional[str] = ...,
        display_name: _Optional[str] = ...,
        role: _Optional[_Union[_member_role_pb2.MemberRole, str]] = ...,
        additional_roles: _Optional[
            _Iterable[_Union[_member_role_pb2.MemberRole, str]]
        ] = ...,
        permissions: _Optional[_Iterable[str]] = ...,
        department_ids: _Optional[_Iterable[str]] = ...,
        team_ids: _Optional[_Iterable[str]] = ...,
        tenant_ids: _Optional[_Iterable[str]] = ...,
        metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_active_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        invited_by: _Optional[str] = ...,
        updated_by: _Optional[str] = ...,
        active: _Optional[bool] = ...,
        job_title: _Optional[str] = ...,
        manager_id: _Optional[str] = ...,
        direct_report_ids: _Optional[_Iterable[str]] = ...,
        avatar_url: _Optional[str] = ...,
        phone: _Optional[str] = ...,
        location: _Optional[str] = ...,
    ) -> None: ...
