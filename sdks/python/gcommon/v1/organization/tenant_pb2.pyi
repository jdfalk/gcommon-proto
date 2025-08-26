import datetime

from gcommon.v1.common import isolation_level_pb2 as _isolation_level_pb2
from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.common import tenant_status_pb2 as _tenant_status_pb2
from gcommon.v1.organization import tenant_quota_pb2 as _tenant_quota_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tenant(_message.Message):
    __slots__ = ("id", "organization_id", "name", "slug", "description", "status", "isolation_level", "metadata", "created_at", "updated_at", "created_by", "updated_by", "database_config", "network_config", "quota", "custom_domain", "timezone", "locale", "trial_mode", "trial_expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    DATABASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_MODE_FIELD_NUMBER: _ClassVar[int]
    TRIAL_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    slug: str
    description: str
    status: _tenant_status_pb2.TenantStatus
    isolation_level: _isolation_level_pb2.OrganizationIsolationLevel
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    created_by: str
    updated_by: str
    database_config: str
    network_config: str
    quota: _tenant_quota_pb2.TenantQuota
    custom_domain: str
    timezone: str
    locale: str
    trial_mode: bool
    trial_expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[_tenant_status_pb2.TenantStatus, str]] = ..., isolation_level: _Optional[_Union[_isolation_level_pb2.OrganizationIsolationLevel, str]] = ..., metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., database_config: _Optional[str] = ..., network_config: _Optional[str] = ..., quota: _Optional[_Union[_tenant_quota_pb2.TenantQuota, _Mapping]] = ..., custom_domain: _Optional[str] = ..., timezone: _Optional[str] = ..., locale: _Optional[str] = ..., trial_mode: _Optional[bool] = ..., trial_expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
