from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.organization import organization_pb2 as _organization_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ("organization", "errors", "success")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    organization: _organization_pb2.Organization
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    def __init__(self, organization: _Optional[_Union[_organization_pb2.Organization, _Mapping]] = ..., errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: bool = ...) -> None: ...
