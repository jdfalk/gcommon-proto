from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteTopicResponse(_message.Message):
    __slots__ = (
        "success",
        "deleted_subscriptions",
        "purged_messages",
        "message",
        "error",
    )
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DELETED_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PURGED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    deleted_subscriptions: int
    purged_messages: int
    message: str
    error: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        deleted_subscriptions: _Optional[int] = ...,
        purged_messages: _Optional[int] = ...,
        message: _Optional[str] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
