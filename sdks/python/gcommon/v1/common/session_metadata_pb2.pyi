from gcommon.v1.common import session_state_pb2 as _session_state_pb2
from gcommon.v1.common import device_info_pb2 as _device_info_pb2
from gcommon.v1.common import location_info_pb2 as _location_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionMetadata(_message.Message):
    __slots__ = ("session_id", "user_id", "started_at", "last_activity", "expires_at", "ip_address", "user_agent", "device_info", "location_info", "state")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_id: str
    started_at: int
    last_activity: int
    expires_at: int
    ip_address: str
    user_agent: str
    device_info: _device_info_pb2.DeviceInfo
    location_info: _location_info_pb2.LocationInfo
    state: _session_state_pb2.AuthSessionState
    def __init__(self, session_id: _Optional[str] = ..., user_id: _Optional[str] = ..., started_at: _Optional[int] = ..., last_activity: _Optional[int] = ..., expires_at: _Optional[int] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., device_info: _Optional[_Union[_device_info_pb2.DeviceInfo, _Mapping]] = ..., location_info: _Optional[_Union[_location_info_pb2.LocationInfo, _Mapping]] = ..., state: _Optional[_Union[_session_state_pb2.AuthSessionState, str]] = ...) -> None: ...
