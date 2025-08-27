from gcommon.v1.metrics import api_key_config_update_pb2 as _api_key_config_update_pb2
from gcommon.v1.metrics import tls_config_update_pb2 as _tls_config_update_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityConfigUpdate(_message.Message):
    __slots__ = ("require_auth", "auth_methods", "require_tls", "tls_config_update", "api_key_config_update")
    REQUIRE_AUTH_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHODS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_TLS_FIELD_NUMBER: _ClassVar[int]
    TLS_CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CONFIG_UPDATE_FIELD_NUMBER: _ClassVar[int]
    require_auth: bool
    auth_methods: _containers.RepeatedScalarFieldContainer[str]
    require_tls: bool
    tls_config_update: _tls_config_update_pb2.TLSConfigUpdate
    api_key_config_update: _api_key_config_update_pb2.APIKeyConfigUpdate
    def __init__(self, require_auth: _Optional[bool] = ..., auth_methods: _Optional[_Iterable[str]] = ..., require_tls: _Optional[bool] = ..., tls_config_update: _Optional[_Union[_tls_config_update_pb2.TLSConfigUpdate, _Mapping]] = ..., api_key_config_update: _Optional[_Union[_api_key_config_update_pb2.APIKeyConfigUpdate, _Mapping]] = ...) -> None: ...
