from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateTokenRequest(_message.Message):
    __slots__ = ("access_token", "metadata", "include_user_info", "include_permissions")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_USER_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    metadata: _request_metadata_pb2.RequestMetadata
    include_user_info: bool
    include_permissions: bool
    def __init__(self, access_token: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., include_user_info: _Optional[bool] = ..., include_permissions: _Optional[bool] = ...) -> None: ...
