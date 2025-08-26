from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetApiKeyRequest(_message.Message):
    __slots__ = ("key_id", "include_stats")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_STATS_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    include_stats: bool
    def __init__(self, key_id: _Optional[str] = ..., include_stats: bool = ...) -> None: ...
