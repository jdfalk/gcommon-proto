from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExportQueueResponse(_message.Message):
    __slots__ = ("export_id", "status", "export_path", "message_count", "data_size_bytes", "format", "start_timestamp", "end_timestamp", "error")
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    export_id: str
    status: str
    export_path: str
    message_count: int
    data_size_bytes: int
    format: str
    start_timestamp: int
    end_timestamp: int
    error: str
    def __init__(self, export_id: _Optional[str] = ..., status: _Optional[str] = ..., export_path: _Optional[str] = ..., message_count: _Optional[int] = ..., data_size_bytes: _Optional[int] = ..., format: _Optional[str] = ..., start_timestamp: _Optional[int] = ..., end_timestamp: _Optional[int] = ..., error: _Optional[str] = ...) -> None: ...
