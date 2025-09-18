from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSubscriptionRequest(_message.Message):
    __slots__ = ("subscription_id", "force", "timeout_ms")
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    force: bool
    timeout_ms: int
    def __init__(self, subscription_id: _Optional[str] = ..., force: _Optional[bool] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
