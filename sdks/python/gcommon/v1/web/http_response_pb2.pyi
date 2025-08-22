from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpResponse(_message.Message):
    __slots__ = ("status_code", "status_message", "protocol_version", "request_metadata", "headers", "body", "cookies", "content_length", "content_type", "content_encoding", "cache_control", "etag", "location", "server", "access_control_allow_origin", "access_control_allow_methods", "access_control_allow_headers", "request_id", "service_name", "service_version", "processing_time_ms", "served_from_cache", "streaming", "keep_alive", "compressed", "compression_ratio", "error", "processing_started_at", "generated_at", "sent_at")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CookiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_METADATA_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    COOKIES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_ALLOW_ORIGIN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_ALLOW_METHODS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CONTROL_ALLOW_HEADERS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SERVED_FROM_CACHE_FIELD_NUMBER: _ClassVar[int]
    STREAMING_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_RATIO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    status_message: str
    protocol_version: str
    request_metadata: _request_metadata_pb2.RequestMetadata
    headers: _containers.ScalarMap[str, str]
    body: _any_pb2.Any
    cookies: _containers.ScalarMap[str, str]
    content_length: int
    content_type: str
    content_encoding: str
    cache_control: str
    etag: str
    location: str
    server: str
    access_control_allow_origin: str
    access_control_allow_methods: str
    access_control_allow_headers: str
    request_id: str
    service_name: str
    service_version: str
    processing_time_ms: int
    served_from_cache: bool
    streaming: bool
    keep_alive: bool
    compressed: bool
    compression_ratio: float
    error: _error_pb2.Error
    processing_started_at: _timestamp_pb2.Timestamp
    generated_at: _timestamp_pb2.Timestamp
    sent_at: _timestamp_pb2.Timestamp
    def __init__(self, status_code: _Optional[int] = ..., status_message: _Optional[str] = ..., protocol_version: _Optional[str] = ..., request_metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., headers: _Optional[_Mapping[str, str]] = ..., body: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., cookies: _Optional[_Mapping[str, str]] = ..., content_length: _Optional[int] = ..., content_type: _Optional[str] = ..., content_encoding: _Optional[str] = ..., cache_control: _Optional[str] = ..., etag: _Optional[str] = ..., location: _Optional[str] = ..., server: _Optional[str] = ..., access_control_allow_origin: _Optional[str] = ..., access_control_allow_methods: _Optional[str] = ..., access_control_allow_headers: _Optional[str] = ..., request_id: _Optional[str] = ..., service_name: _Optional[str] = ..., service_version: _Optional[str] = ..., processing_time_ms: _Optional[int] = ..., served_from_cache: bool = ..., streaming: bool = ..., keep_alive: bool = ..., compressed: bool = ..., compression_ratio: _Optional[float] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., processing_started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., generated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
