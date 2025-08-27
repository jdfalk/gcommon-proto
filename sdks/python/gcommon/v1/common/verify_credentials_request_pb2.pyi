from gcommon.v1.common import api_key_credentials_pb2 as _api_key_credentials_pb2
from gcommon.v1.common import password_credentials_pb2 as _password_credentials_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyCredentialsRequest(_message.Message):
    __slots__ = ("metadata", "password", "api_key")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    password: _password_credentials_pb2.PasswordCredentials
    api_key: _api_key_credentials_pb2.APIKeyCredentials
    def __init__(
        self,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
        password: _Optional[
            _Union[_password_credentials_pb2.PasswordCredentials, _Mapping]
        ] = ...,
        api_key: _Optional[
            _Union[_api_key_credentials_pb2.APIKeyCredentials, _Mapping]
        ] = ...,
    ) -> None: ...
