from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OpenTelemetrySettingsUpdate(_message.Message):
    __slots__ = (
        "endpoint",
        "use_tls",
        "header_updates",
        "header_removes",
        "resource_attribute_updates",
        "resource_attribute_removes",
        "timeout",
    )
    class HeaderUpdatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    class ResourceAttributeUpdatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USE_TLS_FIELD_NUMBER: _ClassVar[int]
    HEADER_UPDATES_FIELD_NUMBER: _ClassVar[int]
    HEADER_REMOVES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ATTRIBUTE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ATTRIBUTE_REMOVES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    use_tls: bool
    header_updates: _containers.ScalarMap[str, str]
    header_removes: _containers.RepeatedScalarFieldContainer[str]
    resource_attribute_updates: _containers.ScalarMap[str, str]
    resource_attribute_removes: _containers.RepeatedScalarFieldContainer[str]
    timeout: str
    def __init__(
        self,
        endpoint: _Optional[str] = ...,
        use_tls: _Optional[bool] = ...,
        header_updates: _Optional[_Mapping[str, str]] = ...,
        header_removes: _Optional[_Iterable[str]] = ...,
        resource_attribute_updates: _Optional[_Mapping[str, str]] = ...,
        resource_attribute_removes: _Optional[_Iterable[str]] = ...,
        timeout: _Optional[str] = ...,
    ) -> None: ...
