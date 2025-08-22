from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StorageBackend(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORAGE_BACKEND_UNSPECIFIED: _ClassVar[StorageBackend]
    STORAGE_BACKEND_MEMORY: _ClassVar[StorageBackend]
    STORAGE_BACKEND_PROMETHEUS: _ClassVar[StorageBackend]
    STORAGE_BACKEND_INFLUXDB: _ClassVar[StorageBackend]
    STORAGE_BACKEND_TIMESCALEDB: _ClassVar[StorageBackend]
    STORAGE_BACKEND_OPENTELEMETRY: _ClassVar[StorageBackend]
    STORAGE_BACKEND_GRAPHITE: _ClassVar[StorageBackend]
    STORAGE_BACKEND_ELASTICSEARCH: _ClassVar[StorageBackend]
    STORAGE_BACKEND_CLOUDWATCH: _ClassVar[StorageBackend]
    STORAGE_BACKEND_GCP_MONITORING: _ClassVar[StorageBackend]
    STORAGE_BACKEND_AZURE_MONITOR: _ClassVar[StorageBackend]
    STORAGE_BACKEND_VICTORIAMETRICS: _ClassVar[StorageBackend]
STORAGE_BACKEND_UNSPECIFIED: StorageBackend
STORAGE_BACKEND_MEMORY: StorageBackend
STORAGE_BACKEND_PROMETHEUS: StorageBackend
STORAGE_BACKEND_INFLUXDB: StorageBackend
STORAGE_BACKEND_TIMESCALEDB: StorageBackend
STORAGE_BACKEND_OPENTELEMETRY: StorageBackend
STORAGE_BACKEND_GRAPHITE: StorageBackend
STORAGE_BACKEND_ELASTICSEARCH: StorageBackend
STORAGE_BACKEND_CLOUDWATCH: StorageBackend
STORAGE_BACKEND_GCP_MONITORING: StorageBackend
STORAGE_BACKEND_AZURE_MONITOR: StorageBackend
STORAGE_BACKEND_VICTORIAMETRICS: StorageBackend
