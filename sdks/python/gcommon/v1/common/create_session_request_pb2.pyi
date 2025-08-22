from gcommon.v1.common import client_info_pb2 as _client_info_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthCreateSessionRequest(_message.Message):
    __slots__ = ("metadata", "user_id", "client_info", "duration_seconds", "session_metadata")
    class SessionMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    user_id: str
    client_info: _client_info_pb2.ClientInfo
    duration_seconds: int
    session_metadata: _containers.ScalarMap[str, str]
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., user_id: _Optional[str] = ..., client_info: _Optional[_Union[_client_info_pb2.ClientInfo, _Mapping]] = ..., duration_seconds: _Optional[int] = ..., session_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
