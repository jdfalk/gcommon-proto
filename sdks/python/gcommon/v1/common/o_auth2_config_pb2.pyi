from gcommon.v1.common import jwt_config_pb2 as _jwt_config_pb2
from gcommon.v1.common import oauth2_flow_type_pb2 as _oauth2_flow_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAuth2Config(_message.Message):
    __slots__ = ("provider_name", "client_id", "client_secret", "authorization_endpoint", "token_endpoint", "userinfo_endpoint", "redirect_uri", "scopes", "flow_type", "additional_params", "require_pkce", "jwt_config")
    class AdditionalParamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    FLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PKCE_FIELD_NUMBER: _ClassVar[int]
    JWT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    provider_name: str
    client_id: str
    client_secret: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    redirect_uri: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    flow_type: _oauth2_flow_type_pb2.OAuth2FlowType
    additional_params: _containers.ScalarMap[str, str]
    require_pkce: bool
    jwt_config: _jwt_config_pb2.JWTConfig
    def __init__(self, provider_name: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., authorization_endpoint: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., flow_type: _Optional[_Union[_oauth2_flow_type_pb2.OAuth2FlowType, str]] = ..., additional_params: _Optional[_Mapping[str, str]] = ..., require_pkce: bool = ..., jwt_config: _Optional[_Union[_jwt_config_pb2.JWTConfig, _Mapping]] = ...) -> None: ...
