import datetime

from gcommon.v1.common import proxy_type_pb2 as _proxy_type_pb2
from gcommon.v1.web import http_header_pb2 as _http_header_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProxyConfig(_message.Message):
    __slots__ = (
        "proxy_type",
        "target_url",
        "forward_headers",
        "connect_timeout",
        "trust_forward_headers",
    )
    PROXY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    FORWARD_HEADERS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRUST_FORWARD_HEADERS_FIELD_NUMBER: _ClassVar[int]
    proxy_type: _proxy_type_pb2.ProxyType
    target_url: str
    forward_headers: _containers.RepeatedCompositeFieldContainer[
        _http_header_pb2.HttpHeader
    ]
    connect_timeout: _duration_pb2.Duration
    trust_forward_headers: bool
    def __init__(
        self,
        proxy_type: _Optional[_Union[_proxy_type_pb2.ProxyType, str]] = ...,
        target_url: _Optional[str] = ...,
        forward_headers: _Optional[
            _Iterable[_Union[_http_header_pb2.HttpHeader, _Mapping]]
        ] = ...,
        connect_timeout: _Optional[
            _Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]
        ] = ...,
        trust_forward_headers: _Optional[bool] = ...,
    ) -> None: ...
