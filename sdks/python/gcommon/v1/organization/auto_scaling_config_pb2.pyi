from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AutoScalingConfig(_message.Message):
    __slots__ = ("enabled", "min_instances", "max_instances", "target_cpu_percent", "target_memory_percent", "scale_up_cooldown", "scale_down_cooldown")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_CPU_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEMORY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SCALE_UP_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    SCALE_DOWN_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    min_instances: int
    max_instances: int
    target_cpu_percent: int
    target_memory_percent: int
    scale_up_cooldown: int
    scale_down_cooldown: int
    def __init__(self, enabled: bool = ..., min_instances: _Optional[int] = ..., max_instances: _Optional[int] = ..., target_cpu_percent: _Optional[int] = ..., target_memory_percent: _Optional[int] = ..., scale_up_cooldown: _Optional[int] = ..., scale_down_cooldown: _Optional[int] = ...) -> None: ...
