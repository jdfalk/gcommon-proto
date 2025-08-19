from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpRequest(_message.Message):
    __slots__ = ("method", "url", "protocol_version", "metadata", "headers", "body", "query_params", "path_params", "cookies", "client_ip", "user_agent", "referrer", "content_length", "content_type", "accept", "accept_language", "accept_encoding", "authorization", "request_id", "session_id", "target_service", "target_version", "timeout_ms", "streaming", "keep_alive", "received_at", "created_at")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class QueryParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PathParamsEntry(_message.Message):
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
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PATH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    COOKIES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TARGET_VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    STREAMING_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    method: str
    url: str
    protocol_version: str
    metadata: _request_metadata_pb2.RequestMetadata
    headers: _containers.ScalarMap[str, str]
    body: _any_pb2.Any
    query_params: _containers.ScalarMap[str, str]
    path_params: _containers.ScalarMap[str, str]
    cookies: _containers.ScalarMap[str, str]
    client_ip: str
    user_agent: str
    referrer: str
    content_length: int
    content_type: str
    accept: str
    accept_language: str
    accept_encoding: str
    authorization: str
    request_id: str
    session_id: str
    target_service: str
    target_version: str
    timeout_ms: int
    streaming: bool
    keep_alive: bool
    received_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, method: _Optional[str] = ..., url: _Optional[str] = ..., protocol_version: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., headers: _Optional[_Mapping[str, str]] = ..., body: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., query_params: _Optional[_Mapping[str, str]] = ..., path_params: _Optional[_Mapping[str, str]] = ..., cookies: _Optional[_Mapping[str, str]] = ..., client_ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., referrer: _Optional[str] = ..., content_length: _Optional[int] = ..., content_type: _Optional[str] = ..., accept: _Optional[str] = ..., accept_language: _Optional[str] = ..., accept_encoding: _Optional[str] = ..., authorization: _Optional[str] = ..., request_id: _Optional[str] = ..., session_id: _Optional[str] = ..., target_service: _Optional[str] = ..., target_version: _Optional[str] = ..., timeout_ms: _Optional[int] = ..., streaming: bool = ..., keep_alive: bool = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
