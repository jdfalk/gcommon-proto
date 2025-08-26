from gcommon.v1.common import metrics_api_key_config_pb2 as _metrics_api_key_config_pb2
from gcommon.v1.metrics import tls_config_pb2 as _tls_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsSecurityConfig(_message.Message):
    __slots__ = ("require_auth", "auth_methods", "require_tls", "tls_config", "api_key_config")
    REQUIRE_AUTH_FIELD_NUMBER: _ClassVar[int]
    AUTH_METHODS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_TLS_FIELD_NUMBER: _ClassVar[int]
    TLS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    API_KEY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    require_auth: bool
    auth_methods: _containers.RepeatedScalarFieldContainer[str]
    require_tls: bool
    tls_config: _tls_config_pb2.MetricsTLSConfig
    api_key_config: _metrics_api_key_config_pb2.MetricsAPIKeyConfig
    def __init__(self, require_auth: bool = ..., auth_methods: _Optional[_Iterable[str]] = ..., require_tls: bool = ..., tls_config: _Optional[_Union[_tls_config_pb2.MetricsTLSConfig, _Mapping]] = ..., api_key_config: _Optional[_Union[_metrics_api_key_config_pb2.MetricsAPIKeyConfig, _Mapping]] = ...) -> None: ...
