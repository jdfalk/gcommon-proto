from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization import organization_pb2 as _organization_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("metadata", "organization_id", "organization", "update_fields")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    organization_id: str
    organization: _organization_pb2.Organization
    update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., organization_id: _Optional[str] = ..., organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ..., update_fields: _Optional[_Iterable[str]] = ...) -> None: ...
