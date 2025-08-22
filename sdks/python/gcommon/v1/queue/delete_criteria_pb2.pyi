from gcommon.v1.queue import message_state_pb2 as _message_state_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteCriteria(_message.Message):
    __slots__ = ("older_than_timestamp", "header_filters", "priority", "correlation_id", "max_messages", "state")
    class HeaderFiltersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OLDER_THAN_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HEADER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    older_than_timestamp: int
    header_filters: _containers.ScalarMap[str, str]
    priority: int
    correlation_id: str
    max_messages: int
    state: _message_state_pb2.MessageState
    def __init__(self, older_than_timestamp: _Optional[int] = ..., header_filters: _Optional[_Mapping[str, str]] = ..., priority: _Optional[int] = ..., correlation_id: _Optional[str] = ..., max_messages: _Optional[int] = ..., state: _Optional[_Union[_message_state_pb2.MessageState, str]] = ...) -> None: ...
