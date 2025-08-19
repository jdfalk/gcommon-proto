from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderFilter(_message.Message):
    __slots__ = ("provider_types", "states", "tags", "name_pattern", "health_statuses", "created_after", "created_before")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROVIDER_TYPES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUSES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    provider_types: _containers.RepeatedScalarFieldContainer[str]
    states: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.ScalarMap[str, str]
    name_pattern: str
    health_statuses: _containers.RepeatedScalarFieldContainer[str]
    created_after: str
    created_before: str
    def __init__(self, provider_types: _Optional[_Iterable[str]] = ..., states: _Optional[_Iterable[str]] = ..., tags: _Optional[_Mapping[str, str]] = ..., name_pattern: _Optional[str] = ..., health_statuses: _Optional[_Iterable[str]] = ..., created_after: _Optional[str] = ..., created_before: _Optional[str] = ...) -> None: ...
