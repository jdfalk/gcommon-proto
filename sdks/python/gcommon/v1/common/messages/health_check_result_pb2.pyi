from gcommon.v1.common.enums import check_type_pb2 as _check_type_pb2
from gcommon.v1.common.enums import serving_status_pb2 as _serving_status_pb2
from gcommon.v1.common.messages import component_health_pb2 as _component_health_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthHealthCheckResult(_message.Message):
    __slots__ = ("service", "status", "check_type", "timestamp", "duration_ms", "message", "error", "metadata", "components")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    service: str
    status: _serving_status_pb2.ServingStatus
    check_type: _check_type_pb2.CheckType
    timestamp: int
    duration_ms: int
    message: str
    error: str
    metadata: _containers.ScalarMap[str, str]
    components: _containers.RepeatedCompositeFieldContainer[_component_health_pb2.ComponentHealth]
    def __init__(self, service: _Optional[str] = ..., status: _Optional[_Union[_serving_status_pb2.ServingStatus, str]] = ..., check_type: _Optional[_Union[_check_type_pb2.CheckType, str]] = ..., timestamp: _Optional[int] = ..., duration_ms: _Optional[int] = ..., message: _Optional[str] = ..., error: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., components: _Optional[_Iterable[_Union[_component_health_pb2.ComponentHealth, _Mapping]]] = ...) -> None: ...
