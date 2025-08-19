from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import provider_status_pb2 as _provider_status_pb2
from gcommon.v1.metrics.messages import validation_result_pb2 as _validation_result_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateProviderResponse(_message.Message):
    __slots__ = ("success", "provider_id", "status", "validation_results", "error", "updated_at", "applied_changes", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    APPLIED_CHANGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    provider_id: str
    status: _provider_status_pb2.ProviderStatus
    validation_results: _containers.RepeatedCompositeFieldContainer[_validation_result_pb2.MetricsValidationResult]
    error: _error_pb2.Error
    updated_at: _timestamp_pb2.Timestamp
    applied_changes: _containers.RepeatedScalarFieldContainer[str]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., provider_id: _Optional[str] = ..., status: _Optional[_Union[_provider_status_pb2.ProviderStatus, _Mapping]] = ..., validation_results: _Optional[_Iterable[_Union[_validation_result_pb2.MetricsValidationResult, _Mapping]]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., applied_changes: _Optional[_Iterable[str]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
