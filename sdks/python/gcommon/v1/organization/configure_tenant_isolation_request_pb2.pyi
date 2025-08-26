from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import tenant_isolation_pb2 as _tenant_isolation_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureTenantIsolationRequest(_message.Message):
    __slots__ = ("metadata", "tenant_id", "isolation")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    tenant_id: str
    isolation: _tenant_isolation_pb2.TenantIsolation
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., tenant_id: _Optional[str] = ..., isolation: _Optional[_Union[_tenant_isolation_pb2.TenantIsolation, _Mapping]] = ...) -> None: ...
