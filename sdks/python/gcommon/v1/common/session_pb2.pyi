import datetime

from gcommon.v1.common import client_info_pb2 as _client_info_pb2
from gcommon.v1.common import session_status_pb2 as _session_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = (
        "id",
        "user_id",
        "created_at",
        "last_activity_at",
        "expires_at",
        "client_info",
        "status",
        "metadata",
        "ip_address",
        "user_agent",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    created_at: _timestamp_pb2.Timestamp
    last_activity_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    client_info: _client_info_pb2.ClientInfo
    status: _session_status_pb2.SessionStatus
    metadata: _containers.ScalarMap[str, str]
    ip_address: str
    user_agent: str
    def __init__(
        self,
        id: _Optional[str] = ...,
        user_id: _Optional[str] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        last_activity_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        expires_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        client_info: _Optional[_Union[_client_info_pb2.ClientInfo, _Mapping]] = ...,
        status: _Optional[_Union[_session_status_pb2.SessionStatus, str]] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
        ip_address: _Optional[str] = ...,
        user_agent: _Optional[str] = ...,
    ) -> None: ...
