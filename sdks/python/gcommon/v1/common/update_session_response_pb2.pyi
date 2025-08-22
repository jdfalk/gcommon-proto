from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from gcommon.v1.common import session_info_pb2 as _session_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthUpdateSessionResponse(_message.Message):
    __slots__ = ("success", "session", "error_message", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    session: _session_info_pb2.SessionInfo
    error_message: str
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, success: bool = ..., session: _Optional[_Union[_session_info_pb2.SessionInfo, _Mapping]] = ..., error_message: _Optional[str] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
