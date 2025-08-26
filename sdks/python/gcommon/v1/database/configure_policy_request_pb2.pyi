from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigurePolicyRequest(_message.Message):
    __slots__ = ("namespace_id", "eviction_policy", "max_ttl_seconds", "memory_threshold_percent", "policy_config")
    class PolicyConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EVICTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAX_TTL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_THRESHOLD_PERCENT_FIELD_NUMBER: _ClassVar[int]
    POLICY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    namespace_id: str
    eviction_policy: str
    max_ttl_seconds: int
    memory_threshold_percent: float
    policy_config: _containers.ScalarMap[str, str]
    def __init__(self, namespace_id: _Optional[str] = ..., eviction_policy: _Optional[str] = ..., max_ttl_seconds: _Optional[int] = ..., memory_threshold_percent: _Optional[float] = ..., policy_config: _Optional[_Mapping[str, str]] = ...) -> None: ...
