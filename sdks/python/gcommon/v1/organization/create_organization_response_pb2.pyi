from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.organization import organization_pb2 as _organization_pb2
from gcommon.v1.organization import tenant_pb2 as _tenant_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrganizationResponse(_message.Message):
    __slots__ = (
        "organization",
        "default_tenant",
        "owner_member_id",
        "errors",
        "success",
        "message",
    )
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TENANT_FIELD_NUMBER: _ClassVar[int]
    OWNER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    default_tenant: _tenant_pb2.Tenant
    owner_member_id: str
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    message: str
    def __init__(
        self,
        organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ...,
        default_tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...,
        owner_member_id: _Optional[str] = ...,
        errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ...,
        success: _Optional[bool] = ...,
        message: _Optional[str] = ...,
    ) -> None: ...
