from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.organization.messages import organization_pb2 as _organization_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("metadata", "organization", "create_default_tenant", "initial_settings_json", "owner_user_id", "send_welcome_email", "organization_template")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_DEFAULT_TENANT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SETTINGS_JSON_FIELD_NUMBER: _ClassVar[int]
    OWNER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SEND_WELCOME_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    organization: _organization_pb2.Organization
    create_default_tenant: bool
    initial_settings_json: str
    owner_user_id: str
    send_welcome_email: bool
    organization_template: str
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ..., create_default_tenant: bool = ..., initial_settings_json: _Optional[str] = ..., owner_user_id: _Optional[str] = ..., send_welcome_email: bool = ..., organization_template: _Optional[str] = ...) -> None: ...
