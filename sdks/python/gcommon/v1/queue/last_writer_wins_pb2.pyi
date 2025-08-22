from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LastWriterWins(_message.Message):
    __slots__ = ("use_server_timestamp", "timestamp_precision")
    USE_SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_PRECISION_FIELD_NUMBER: _ClassVar[int]
    use_server_timestamp: bool
    timestamp_precision: str
    def __init__(self, use_server_timestamp: bool = ..., timestamp_precision: _Optional[str] = ...) -> None: ...
