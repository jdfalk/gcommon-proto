from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TerminateSessionRequest(_message.Message):
    __slots__ = ("user_id", "session_ids", "metadata", "terminate_all", "device_type_filter", "created_before", "last_activity_before", "exclude_current_session", "termination_reason", "send_notification", "force_immediate")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TERMINATE_ALL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_BEFORE_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_BEFORE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CURRENT_SESSION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_REASON_FIELD_NUMBER: _ClassVar[int]
    SEND_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    FORCE_IMMEDIATE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    session_ids: _containers.RepeatedScalarFieldContainer[str]
    metadata: _request_metadata_pb2.RequestMetadata
    terminate_all: bool
    device_type_filter: str
    created_before: _timestamp_pb2.Timestamp
    last_activity_before: _timestamp_pb2.Timestamp
    exclude_current_session: bool
    termination_reason: str
    send_notification: bool
    force_immediate: bool
    def __init__(self, user_id: _Optional[str] = ..., session_ids: _Optional[_Iterable[str]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., terminate_all: bool = ..., device_type_filter: _Optional[str] = ..., created_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_activity_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exclude_current_session: bool = ..., termination_reason: _Optional[str] = ..., send_notification: bool = ..., force_immediate: bool = ...) -> None: ...
