from gcommon.v1.common.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheInfo(_message.Message):
    __slots__ = ("name", "version", "cache_type", "health_status", "created_at", "last_accessed", "instance_id", "description", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CACHE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESSED_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    cache_type: str
    health_status: _health_status_pb2.CommonHealthStatus
    created_at: _timestamp_pb2.Timestamp
    last_accessed: _timestamp_pb2.Timestamp
    instance_id: str
    description: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., cache_type: _Optional[str] = ..., health_status: _Optional[_Union[_health_status_pb2.CommonHealthStatus, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_accessed: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instance_id: _Optional[str] = ..., description: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
