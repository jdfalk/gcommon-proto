from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TenantQuota(_message.Message):
    __slots__ = ("tenant_id", "max_users", "max_storage_bytes", "max_api_requests_per_hour", "max_projects", "max_bandwidth_bytes_per_month", "can_create_sub_tenants", "custom_quotas")
    class CustomQuotasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_USERS_FIELD_NUMBER: _ClassVar[int]
    MAX_STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_API_REQUESTS_PER_HOUR_FIELD_NUMBER: _ClassVar[int]
    MAX_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    MAX_BANDWIDTH_BYTES_PER_MONTH_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_SUB_TENANTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_QUOTAS_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    max_users: int
    max_storage_bytes: int
    max_api_requests_per_hour: int
    max_projects: int
    max_bandwidth_bytes_per_month: int
    can_create_sub_tenants: bool
    custom_quotas: _containers.ScalarMap[str, str]
    def __init__(self, tenant_id: _Optional[str] = ..., max_users: _Optional[int] = ..., max_storage_bytes: _Optional[int] = ..., max_api_requests_per_hour: _Optional[int] = ..., max_projects: _Optional[int] = ..., max_bandwidth_bytes_per_month: _Optional[int] = ..., can_create_sub_tenants: bool = ..., custom_quotas: _Optional[_Mapping[str, str]] = ...) -> None: ...
