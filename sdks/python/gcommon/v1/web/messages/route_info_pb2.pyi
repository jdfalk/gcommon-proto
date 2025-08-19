from gcommon.v1.web.enums import route_type_pb2 as _route_type_pb2
from gcommon.v1.web.messages import route_config_pb2 as _route_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RouteInfo(_message.Message):
    __slots__ = ("config", "route_type", "created_at", "updated_at")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    config: _route_config_pb2.RouteConfig
    route_type: _route_type_pb2.RouteType
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, config: _Optional[_Union[_route_config_pb2.RouteConfig, _Mapping]] = ..., route_type: _Optional[_Union[_route_type_pb2.RouteType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
