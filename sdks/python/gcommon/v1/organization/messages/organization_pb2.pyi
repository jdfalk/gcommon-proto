from gcommon.v1.common.messages import key_value_pb2 as _key_value_pb2
from gcommon.v1.organization.enums import organization_status_pb2 as _organization_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ("id", "name", "slug", "description", "website", "contact_email", "address", "phone", "tax_id", "industry", "status", "metadata", "created_at", "updated_at", "created_by", "updated_by", "timezone", "locale", "max_members", "multi_tenant_enabled", "avatar_url", "billing_email")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MULTI_TENANT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    BILLING_EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    slug: str
    description: str
    website: str
    contact_email: str
    address: str
    phone: str
    tax_id: str
    industry: str
    status: _organization_status_pb2.OrganizationStatus
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    updated_by: str
    timezone: str
    locale: str
    max_members: int
    multi_tenant_enabled: bool
    avatar_url: str
    billing_email: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., website: _Optional[str] = ..., contact_email: _Optional[str] = ..., address: _Optional[str] = ..., phone: _Optional[str] = ..., tax_id: _Optional[str] = ..., industry: _Optional[str] = ..., status: _Optional[_Union[_organization_status_pb2.OrganizationStatus, str]] = ..., metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., timezone: _Optional[str] = ..., locale: _Optional[str] = ..., max_members: _Optional[int] = ..., multi_tenant_enabled: bool = ..., avatar_url: _Optional[str] = ..., billing_email: _Optional[str] = ...) -> None: ...
