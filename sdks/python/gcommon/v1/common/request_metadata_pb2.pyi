from gcommon.v1.common import client_info_pb2 as _client_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestMetadata(_message.Message):
    __slots__ = ("trace_id", "user_id", "correlation_id", "headers", "client", "timestamp", "session_id")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    user_id: str
    correlation_id: str
    headers: _containers.ScalarMap[str, str]
    client: _client_info_pb2.ClientInfo
    timestamp: _timestamp_pb2.Timestamp
    session_id: str
    def __init__(self, trace_id: _Optional[str] = ..., user_id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., client: _Optional[_Union[_client_info_pb2.ClientInfo, _Mapping]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...
