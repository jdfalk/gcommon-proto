from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubscriptionResponse(_message.Message):
    __slots__ = ("success", "error_message", "subscription_id", "subscription_name", "created_at", "initial_position")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_POSITION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error_message: str
    subscription_id: str
    subscription_name: str
    created_at: int
    initial_position: int
    def __init__(self, success: bool = ..., error_message: _Optional[str] = ..., subscription_id: _Optional[str] = ..., subscription_name: _Optional[str] = ..., created_at: _Optional[int] = ..., initial_position: _Optional[int] = ...) -> None: ...
