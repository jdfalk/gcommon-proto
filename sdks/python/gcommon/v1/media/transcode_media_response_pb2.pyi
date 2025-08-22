from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TranscodeMediaResponse(_message.Message):
    __slots__ = ("job_id", "status", "output_file_id", "progress_percent", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: str
    output_file_id: str
    progress_percent: int
    error_message: str
    def __init__(self, job_id: _Optional[str] = ..., status: _Optional[str] = ..., output_file_id: _Optional[str] = ..., progress_percent: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...
