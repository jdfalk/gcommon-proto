from gcommon.v1.organization import auto_scaling_config_pb2 as _auto_scaling_config_pb2
from gcommon.v1.organization import cpu_allocation_pb2 as _cpu_allocation_pb2
from gcommon.v1.organization import memory_allocation_pb2 as _memory_allocation_pb2
from gcommon.v1.organization import resource_limits_pb2 as _resource_limits_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComputeIsolation(_message.Message):
    __slots__ = ("compute_instance", "namespace", "cpu", "memory", "dedicated_compute", "limits", "auto_scaling")
    COMPUTE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_COMPUTE_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCALING_FIELD_NUMBER: _ClassVar[int]
    compute_instance: str
    namespace: str
    cpu: _cpu_allocation_pb2.CPUAllocation
    memory: _memory_allocation_pb2.MemoryAllocation
    dedicated_compute: bool
    limits: _resource_limits_pb2.OrganizationResourceLimits
    auto_scaling: _auto_scaling_config_pb2.AutoScalingConfig
    def __init__(self, compute_instance: _Optional[str] = ..., namespace: _Optional[str] = ..., cpu: _Optional[_Union[_cpu_allocation_pb2.CPUAllocation, _Mapping]] = ..., memory: _Optional[_Union[_memory_allocation_pb2.MemoryAllocation, _Mapping]] = ..., dedicated_compute: bool = ..., limits: _Optional[_Union[_resource_limits_pb2.OrganizationResourceLimits, _Mapping]] = ..., auto_scaling: _Optional[_Union[_auto_scaling_config_pb2.AutoScalingConfig, _Mapping]] = ...) -> None: ...
