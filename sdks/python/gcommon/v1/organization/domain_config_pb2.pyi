from gcommon.v1.organization import dns_config_pb2 as _dns_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainConfig(_message.Message):
    __slots__ = ("domain_name", "ssl_certificate", "dns", "validation_status")
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    SSL_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    DNS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    domain_name: str
    ssl_certificate: str
    dns: _dns_config_pb2.DNSConfig
    validation_status: str
    def __init__(self, domain_name: _Optional[str] = ..., ssl_certificate: _Optional[str] = ..., dns: _Optional[_Union[_dns_config_pb2.DNSConfig, _Mapping]] = ..., validation_status: _Optional[str] = ...) -> None: ...
