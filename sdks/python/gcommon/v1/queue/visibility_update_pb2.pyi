from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VisibilityUpdate(_message.Message):
    __slots__ = ("visibility_timeout_ms", "extend_current", "max_visibility_ms")
    VISIBILITY_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    EXTEND_CURRENT_FIELD_NUMBER: _ClassVar[int]
    MAX_VISIBILITY_MS_FIELD_NUMBER: _ClassVar[int]
    visibility_timeout_ms: int
    extend_current: bool
    max_visibility_ms: int
    def __init__(
        self,
        visibility_timeout_ms: _Optional[int] = ...,
        extend_current: _Optional[bool] = ...,
        max_visibility_ms: _Optional[int] = ...,
    ) -> None: ...
