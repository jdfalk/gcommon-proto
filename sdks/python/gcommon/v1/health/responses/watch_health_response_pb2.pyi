from gcommon.v1.health.messages import health_result_pb2 as _health_result_pb2
from gcommon.v1.health.messages import health_event_pb2 as _health_event_pb2
from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchHealthResponse(_message.Message):
    __slots__ = ("update_type", "result", "event", "metadata")
    UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    update_type: str
    result: _health_result_pb2.HealthResult
    event: _health_event_pb2.HealthEvent
    metadata: _response_metadata_pb2.ResponseMetadata
    def __init__(self, update_type: _Optional[str] = ..., result: _Optional[_Union[_health_result_pb2.HealthResult, _Mapping]] = ..., event: _Optional[_Union[_health_event_pb2.HealthEvent, _Mapping]] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...
