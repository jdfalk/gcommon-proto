from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnsubscribeResponse(_message.Message):
    __slots__ = ("success", "subscription_name", "unsubscribed_at", "lost_messages", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    UNSUBSCRIBED_AT_FIELD_NUMBER: _ClassVar[int]
    LOST_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    subscription_name: str
    unsubscribed_at: _timestamp_pb2.Timestamp
    lost_messages: int
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., subscription_name: _Optional[str] = ..., unsubscribed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lost_messages: _Optional[int] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
