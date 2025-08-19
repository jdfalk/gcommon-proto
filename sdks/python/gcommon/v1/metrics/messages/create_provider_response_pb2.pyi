from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import applied_config_pb2 as _applied_config_pb2
from gcommon.v1.metrics.messages import provider_endpoints_pb2 as _provider_endpoints_pb2
from gcommon.v1.metrics.messages import provider_status_pb2 as _provider_status_pb2
from gcommon.v1.metrics.messages import validation_result_pb2 as _validation_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProviderResponse(_message.Message):
    __slots__ = ("success", "error", "provider_id", "created_at", "status", "validation", "applied_config", "warnings", "endpoints")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    provider_id: str
    created_at: _timestamp_pb2.Timestamp
    status: _provider_status_pb2.ProviderStatus
    validation: _validation_result_pb2.MetricsValidationResult
    applied_config: _applied_config_pb2.AppliedConfig
    warnings: _containers.RepeatedScalarFieldContainer[str]
    endpoints: _provider_endpoints_pb2.ProviderEndpoints
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., provider_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[_provider_status_pb2.ProviderStatus, _Mapping]] = ..., validation: _Optional[_Union[_validation_result_pb2.MetricsValidationResult, _Mapping]] = ..., applied_config: _Optional[_Union[_applied_config_pb2.AppliedConfig, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., endpoints: _Optional[_Union[_provider_endpoints_pb2.ProviderEndpoints, _Mapping]] = ...) -> None: ...
