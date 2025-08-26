from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOrganizationRequest(_message.Message):
    __slots__ = ("metadata", "organization_id", "include_settings", "include_member_count", "include_tenants")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TENANTS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    organization_id: str
    include_settings: bool
    include_member_count: bool
    include_tenants: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., organization_id: _Optional[str] = ..., include_settings: _Optional[bool] = ..., include_member_count: _Optional[bool] = ..., include_tenants: _Optional[bool] = ...) -> None: ...
