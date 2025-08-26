from gcommon.v1.common import api_key_credentials_pb2 as _api_key_credentials_pb2
from gcommon.v1.common import client_info_pb2 as _client_info_pb2
from gcommon.v1.common import jwt_credentials_pb2 as _jwt_credentials_pb2
from gcommon.v1.common import o_auth2_credentials_pb2 as _o_auth2_credentials_pb2
from gcommon.v1.common import password_credentials_pb2 as _password_credentials_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAuthenticateRequest(_message.Message):
    __slots__ = ("metadata", "password", "api_key", "oauth2", "jwt", "scopes", "client_info")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_FIELD_NUMBER: _ClassVar[int]
    JWT_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    password: _password_credentials_pb2.PasswordCredentials
    api_key: _api_key_credentials_pb2.APIKeyCredentials
    oauth2: _o_auth2_credentials_pb2.OAuth2Credentials
    jwt: _jwt_credentials_pb2.JWTCredentials
    scopes: _containers.RepeatedScalarFieldContainer[str]
    client_info: _client_info_pb2.ClientInfo
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., password: _Optional[_Union[_password_credentials_pb2.PasswordCredentials, _Mapping]] = ..., api_key: _Optional[_Union[_api_key_credentials_pb2.APIKeyCredentials, _Mapping]] = ..., oauth2: _Optional[_Union[_o_auth2_credentials_pb2.OAuth2Credentials, _Mapping]] = ..., jwt: _Optional[_Union[_jwt_credentials_pb2.JWTCredentials, _Mapping]] = ..., scopes: _Optional[_Iterable[str]] = ..., client_info: _Optional[_Union[_client_info_pb2.ClientInfo, _Mapping]] = ...) -> None: ...
