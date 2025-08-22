from gcommon.v1.metrics import resource_allocations_pb2 as _resource_allocations_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppliedConfig(_message.Message):
    __slots__ = ("config_summary", "applied_defaults", "applied_overrides", "resource_allocations")
    class AppliedDefaultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AppliedOverridesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CONFIG_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    APPLIED_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    config_summary: str
    applied_defaults: _containers.ScalarMap[str, str]
    applied_overrides: _containers.ScalarMap[str, str]
    resource_allocations: _resource_allocations_pb2.ResourceAllocations
    def __init__(self, config_summary: _Optional[str] = ..., applied_defaults: _Optional[_Mapping[str, str]] = ..., applied_overrides: _Optional[_Mapping[str, str]] = ..., resource_allocations: _Optional[_Union[_resource_allocations_pb2.ResourceAllocations, _Mapping]] = ...) -> None: ...
