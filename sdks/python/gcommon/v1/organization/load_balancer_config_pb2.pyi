from gcommon.v1.organization import health_check_config_pb2 as _health_check_config_pb2
from gcommon.v1.organization import ssl_config_pb2 as _ssl_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationLoadBalancerConfig(_message.Message):
    __slots__ = ("type", "algorithm", "health_check", "ssl")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    SSL_FIELD_NUMBER: _ClassVar[int]
    type: str
    algorithm: str
    health_check: _health_check_config_pb2.OrganizationHealthCheckConfig
    ssl: _ssl_config_pb2.SSLConfig
    def __init__(self, type: _Optional[str] = ..., algorithm: _Optional[str] = ..., health_check: _Optional[_Union[_health_check_config_pb2.OrganizationHealthCheckConfig, _Mapping]] = ..., ssl: _Optional[_Union[_ssl_config_pb2.SSLConfig, _Mapping]] = ...) -> None: ...
