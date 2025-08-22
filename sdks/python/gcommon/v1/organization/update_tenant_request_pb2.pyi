from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import tenant_pb2 as _tenant_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateTenantRequest(_message.Message):
    __slots__ = ("metadata", "tenant_id", "tenant", "update_mask", "validate_only")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    tenant_id: str
    tenant: _tenant_pb2.Tenant
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., tenant_id: _Optional[str] = ..., tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., validate_only: bool = ...) -> None: ...
