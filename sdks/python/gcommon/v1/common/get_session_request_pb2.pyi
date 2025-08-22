from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthGetSessionRequest(_message.Message):
    __slots__ = ("session_id", "include_activity", "metadata")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    include_activity: bool
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, session_id: _Optional[str] = ..., include_activity: bool = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
