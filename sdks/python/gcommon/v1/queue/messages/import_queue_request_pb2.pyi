from gcommon.v1.queue.enums import export_format_pb2 as _export_format_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportQueueRequest(_message.Message):
    __slots__ = ("queue_name", "source_path", "format", "overwrite", "validate", "max_messages", "timeout_ms")
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    queue_name: str
    source_path: str
    format: _export_format_pb2.QueueExportFormat
    overwrite: bool
    validate: bool
    max_messages: int
    timeout_ms: int
    def __init__(self, queue_name: _Optional[str] = ..., source_path: _Optional[str] = ..., format: _Optional[_Union[_export_format_pb2.QueueExportFormat, str]] = ..., overwrite: bool = ..., validate: bool = ..., max_messages: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
