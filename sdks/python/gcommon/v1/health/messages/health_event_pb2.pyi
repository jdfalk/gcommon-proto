from gcommon.v1.health.enums import health_status_pb2 as _health_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthEvent(_message.Message):
    __slots__ = ("event_id", "event_type", "service_name", "check_id", "timestamp", "previous_status", "current_status", "message", "severity", "metadata", "source")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_type: str
    service_name: str
    check_id: str
    timestamp: _timestamp_pb2.Timestamp
    previous_status: _health_status_pb2.HealthStatus
    current_status: _health_status_pb2.HealthStatus
    message: str
    severity: str
    metadata: _containers.ScalarMap[str, str]
    source: str
    def __init__(self, event_id: _Optional[str] = ..., event_type: _Optional[str] = ..., service_name: _Optional[str] = ..., check_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., previous_status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., current_status: _Optional[_Union[_health_status_pb2.HealthStatus, str]] = ..., message: _Optional[str] = ..., severity: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., source: _Optional[str] = ...) -> None: ...
