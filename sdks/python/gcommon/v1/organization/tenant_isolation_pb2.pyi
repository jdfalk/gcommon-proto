import datetime

from gcommon.v1.common import isolation_level_pb2 as _isolation_level_pb2
from gcommon.v1.common import key_value_pb2 as _key_value_pb2
from gcommon.v1.common import (
    organization_access_control_pb2 as _organization_access_control_pb2,
)
from gcommon.v1.organization import audit_config_pb2 as _audit_config_pb2
from gcommon.v1.organization import compute_isolation_pb2 as _compute_isolation_pb2
from gcommon.v1.organization import database_isolation_pb2 as _database_isolation_pb2
from gcommon.v1.organization import encryption_config_pb2 as _encryption_config_pb2
from gcommon.v1.organization import network_isolation_pb2 as _network_isolation_pb2
from gcommon.v1.organization import storage_isolation_pb2 as _storage_isolation_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TenantIsolation(_message.Message):
    __slots__ = (
        "tenant_id",
        "level",
        "database",
        "network",
        "storage",
        "compute",
        "encryption",
        "access_control",
        "audit",
        "metadata",
        "created_at",
        "updated_at",
        "configured_by",
    )
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    AUDIT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURED_BY_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    level: _isolation_level_pb2.OrganizationIsolationLevel
    database: _database_isolation_pb2.DatabaseIsolation
    network: _network_isolation_pb2.NetworkIsolation
    storage: _storage_isolation_pb2.StorageIsolation
    compute: _compute_isolation_pb2.ComputeIsolation
    encryption: _encryption_config_pb2.OrganizationEncryptionConfig
    access_control: _organization_access_control_pb2.OrganizationAccessControl
    audit: _audit_config_pb2.AuditConfig
    metadata: _containers.RepeatedCompositeFieldContainer[_key_value_pb2.KeyValue]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    configured_by: str
    def __init__(
        self,
        tenant_id: _Optional[str] = ...,
        level: _Optional[
            _Union[_isolation_level_pb2.OrganizationIsolationLevel, str]
        ] = ...,
        database: _Optional[
            _Union[_database_isolation_pb2.DatabaseIsolation, _Mapping]
        ] = ...,
        network: _Optional[
            _Union[_network_isolation_pb2.NetworkIsolation, _Mapping]
        ] = ...,
        storage: _Optional[
            _Union[_storage_isolation_pb2.StorageIsolation, _Mapping]
        ] = ...,
        compute: _Optional[
            _Union[_compute_isolation_pb2.ComputeIsolation, _Mapping]
        ] = ...,
        encryption: _Optional[
            _Union[_encryption_config_pb2.OrganizationEncryptionConfig, _Mapping]
        ] = ...,
        access_control: _Optional[
            _Union[_organization_access_control_pb2.OrganizationAccessControl, _Mapping]
        ] = ...,
        audit: _Optional[_Union[_audit_config_pb2.AuditConfig, _Mapping]] = ...,
        metadata: _Optional[_Iterable[_Union[_key_value_pb2.KeyValue, _Mapping]]] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        configured_by: _Optional[str] = ...,
    ) -> None: ...
