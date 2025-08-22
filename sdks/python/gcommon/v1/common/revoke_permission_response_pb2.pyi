from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RevokePermissionResponse(_message.Message):
    __slots__ = ("success", "error_message", "permission_id", "revokee_id", "metadata")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKEE_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    permission_id: str
    revokee_id: str
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ..., permission_id: _Optional[str] = ..., revokee_id: _Optional[str] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
