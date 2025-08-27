from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersioningSettings(_message.Message):
    __slots__ = (
        "enabled",
        "max_versions",
        "retention_days",
        "version_on_change",
        "version_on_schedule",
        "schedule",
        "metadata",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAX_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    VERSION_ON_CHANGE_FIELD_NUMBER: _ClassVar[int]
    VERSION_ON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    max_versions: int
    retention_days: int
    version_on_change: bool
    version_on_schedule: bool
    schedule: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        max_versions: _Optional[int] = ...,
        retention_days: _Optional[int] = ...,
        version_on_change: _Optional[bool] = ...,
        version_on_schedule: _Optional[bool] = ...,
        schedule: _Optional[str] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
