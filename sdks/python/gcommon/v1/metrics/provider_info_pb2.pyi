import datetime

from gcommon.v1.metrics import provider_status_pb2 as _provider_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderInfo(_message.Message):
    __slots__ = (
        "provider_id",
        "name",
        "type",
        "status",
        "detailed_status",
        "config",
        "version",
        "created_at",
        "last_updated",
        "enabled",
        "tags",
        "description",
    )
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILED_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    name: str
    type: str
    status: str
    detailed_status: _provider_status_pb2.ProviderStatus
    config: _containers.ScalarMap[str, str]
    version: str
    created_at: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    enabled: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(
        self,
        provider_id: _Optional[str] = ...,
        name: _Optional[str] = ...,
        type: _Optional[str] = ...,
        status: _Optional[str] = ...,
        detailed_status: _Optional[
            _Union[_provider_status_pb2.ProviderStatus, _Mapping]
        ] = ...,
        config: _Optional[_Mapping[str, str]] = ...,
        version: _Optional[str] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        enabled: _Optional[bool] = ...,
        tags: _Optional[_Iterable[str]] = ...,
        description: _Optional[str] = ...,
    ) -> None: ...
