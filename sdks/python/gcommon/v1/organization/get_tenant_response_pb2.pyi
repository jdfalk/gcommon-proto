from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.organization import tenant_pb2 as _tenant_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTenantResponse(_message.Message):
    __slots__ = ("errors", "success", "tenant")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    tenant: _tenant_pb2.Tenant
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: _Optional[bool] = ..., tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...
