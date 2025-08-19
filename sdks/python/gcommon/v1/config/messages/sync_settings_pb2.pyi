from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SyncSettings(_message.Message):
    __slots__ = ("enabled", "source", "target", "schedule", "filters", "transformations", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    source: str
    target: str
    schedule: str
    filters: _containers.RepeatedScalarFieldContainer[str]
    transformations: _containers.RepeatedScalarFieldContainer[str]
    config: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., source: _Optional[str] = ..., target: _Optional[str] = ..., schedule: _Optional[str] = ..., filters: _Optional[_Iterable[str]] = ..., transformations: _Optional[_Iterable[str]] = ..., config: _Optional[_Mapping[str, str]] = ...) -> None: ...
