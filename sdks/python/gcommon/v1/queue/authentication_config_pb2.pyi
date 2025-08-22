from gcommon.v1.queue import api_key_auth_pb2 as _api_key_auth_pb2
from gcommon.v1.queue import o_auth2_auth_pb2 as _o_auth2_auth_pb2
from gcommon.v1.queue import sasl_auth_pb2 as _sasl_auth_pb2
from gcommon.v1.queue import tls_auth_pb2 as _tls_auth_pb2
from gcommon.v1.queue import username_password_auth_pb2 as _username_password_auth_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthenticationConfig(_message.Message):
    __slots__ = ("none", "username_password", "api_key", "tls", "sasl", "oauth2")
    NONE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    SASL_FIELD_NUMBER: _ClassVar[int]
    OAUTH2_FIELD_NUMBER: _ClassVar[int]
    none: bool
    username_password: _username_password_auth_pb2.UsernamePasswordAuth
    api_key: _api_key_auth_pb2.APIKeyAuth
    tls: _tls_auth_pb2.TLSAuth
    sasl: _sasl_auth_pb2.SASLAuth
    oauth2: _o_auth2_auth_pb2.OAuth2Auth
    def __init__(self, none: bool = ..., username_password: _Optional[_Union[_username_password_auth_pb2.UsernamePasswordAuth, _Mapping]] = ..., api_key: _Optional[_Union[_api_key_auth_pb2.APIKeyAuth, _Mapping]] = ..., tls: _Optional[_Union[_tls_auth_pb2.TLSAuth, _Mapping]] = ..., sasl: _Optional[_Union[_sasl_auth_pb2.SASLAuth, _Mapping]] = ..., oauth2: _Optional[_Union[_o_auth2_auth_pb2.OAuth2Auth, _Mapping]] = ...) -> None: ...
