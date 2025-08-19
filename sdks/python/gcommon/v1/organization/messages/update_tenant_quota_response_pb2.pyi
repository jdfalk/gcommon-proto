from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.organization.messages import tenant_quota_pb2 as _tenant_quota_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateTenantQuotaResponse(_message.Message):
    __slots__ = ("errors", "success", "quota")
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.Error]
    success: bool
    quota: _tenant_quota_pb2.TenantQuota
    def __init__(self, errors: _Optional[_Iterable[_Union[_error_pb2.Error, _Mapping]]] = ..., success: bool = ..., quota: _Optional[_Union[_tenant_quota_pb2.TenantQuota, _Mapping]] = ...) -> None: ...
