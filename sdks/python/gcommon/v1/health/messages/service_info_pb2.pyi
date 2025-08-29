from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceInfo(_message.Message):
    __slots__ = ("name", "version", "status", "description", "registered_at", "last_updated", "endpoints", "tags", "metadata", "check_ids", "monitoring_enabled", "owner")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHECK_IDS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    status: _health_status_pb2.HealthStatus
    description: str
    registered_at: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    endpoints: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    metadata: _containers.ScalarMap[str, str]
    check_ids: _containers.RepeatedScalarFieldContainer[str]
    monitoring_enabled: bool
    owner: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., description: _Optional[str] = ..., registered_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endpoints: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., check_ids: _Optional[_Iterable[str]] = ..., monitoring_enabled: bool = ..., owner: _Optional[str] = ...) -> None: ...
