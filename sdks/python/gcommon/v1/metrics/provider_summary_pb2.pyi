from gcommon.v1.metrics import provider_status_pb2 as _provider_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderSummary(_message.Message):
    __slots__ = ("provider_id", "name", "provider_type", "status", "metric_count", "active_data_points", "storage_size_bytes", "registered_at", "last_updated", "enabled", "performance_score", "health_score", "tags", "description")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METRIC_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DATA_POINTS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_SCORE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    name: str
    provider_type: str
    status: _provider_status_pb2.ProviderStatus
    metric_count: int
    active_data_points: int
    storage_size_bytes: int
    registered_at: _timestamp_pb2.Timestamp
    last_updated: _timestamp_pb2.Timestamp
    enabled: bool
    performance_score: float
    health_score: float
    tags: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, provider_id: _Optional[str] = ..., name: _Optional[str] = ..., provider_type: _Optional[str] = ..., status: _Optional[_Union[_provider_status_pb2.ProviderStatus, _Mapping]] = ..., metric_count: _Optional[int] = ..., active_data_points: _Optional[int] = ..., storage_size_bytes: _Optional[int] = ..., registered_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., enabled: bool = ..., performance_score: _Optional[float] = ..., health_score: _Optional[float] = ..., tags: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...
