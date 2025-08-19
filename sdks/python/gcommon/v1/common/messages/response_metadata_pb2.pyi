from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.common.messages import rate_limit_info_pb2 as _rate_limit_info_pb2
from gcommon.v1.common.messages import pagination_info_pb2 as _pagination_info_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseMetadata(_message.Message):
    __slots__ = ("trace_id", "request_id", "timestamp", "processing_time", "service_version", "success", "error", "metadata", "rate_limit", "pagination")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    request_id: str
    timestamp: _timestamp_pb2.Timestamp
    processing_time: _duration_pb2.Duration
    service_version: str
    success: bool
    error: _error_pb2.Error
    metadata: _containers.ScalarMap[str, str]
    rate_limit: _rate_limit_info_pb2.RateLimitInfo
    pagination: _pagination_info_pb2.CommonPaginationInfo
    def __init__(self, trace_id: _Optional[str] = ..., request_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., processing_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., service_version: _Optional[str] = ..., success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., rate_limit: _Optional[_Union[_rate_limit_info_pb2.RateLimitInfo, _Mapping]] = ..., pagination: _Optional[_Union[_pagination_info_pb2.CommonPaginationInfo, _Mapping]] = ...) -> None: ...
