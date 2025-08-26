from gcommon.v1.metrics import cpu_usage_pb2 as _cpu_usage_pb2
from gcommon.v1.metrics import disk_usage_pb2 as _disk_usage_pb2
from gcommon.v1.metrics import memory_usage_pb2 as _memory_usage_pb2
from gcommon.v1.metrics import network_usage_pb2 as _network_usage_pb2
from gcommon.v1.metrics import resource_data_point_pb2 as _resource_data_point_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUsageStats(_message.Message):
    __slots__ = ("memory", "cpu", "disk", "network", "resource_timeseries")
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    CPU_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    memory: _memory_usage_pb2.MemoryUsage
    cpu: _cpu_usage_pb2.CPUUsage
    disk: _disk_usage_pb2.DiskUsage
    network: _network_usage_pb2.NetworkUsage
    resource_timeseries: _containers.RepeatedCompositeFieldContainer[_resource_data_point_pb2.ResourceDataPoint]
    def __init__(self, memory: _Optional[_Union[_memory_usage_pb2.MemoryUsage, _Mapping]] = ..., cpu: _Optional[_Union[_cpu_usage_pb2.CPUUsage, _Mapping]] = ..., disk: _Optional[_Union[_disk_usage_pb2.DiskUsage, _Mapping]] = ..., network: _Optional[_Union[_network_usage_pb2.NetworkUsage, _Mapping]] = ..., resource_timeseries: _Optional[_Iterable[_Union[_resource_data_point_pb2.ResourceDataPoint, _Mapping]]] = ...) -> None: ...
