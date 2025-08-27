from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderEndpoints(_message.Message):
    __slots__ = (
        "service_endpoint",
        "metrics_endpoint",
        "health_endpoint",
        "admin_endpoint",
        "additional_endpoints",
    )
    class AdditionalEndpointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    SERVICE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METRICS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    service_endpoint: str
    metrics_endpoint: str
    health_endpoint: str
    admin_endpoint: str
    additional_endpoints: _containers.ScalarMap[str, str]
    def __init__(
        self,
        service_endpoint: _Optional[str] = ...,
        metrics_endpoint: _Optional[str] = ...,
        health_endpoint: _Optional[str] = ...,
        admin_endpoint: _Optional[str] = ...,
        additional_endpoints: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
