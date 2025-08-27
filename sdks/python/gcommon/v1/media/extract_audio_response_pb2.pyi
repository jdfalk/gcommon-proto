from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractAudioResponse(_message.Message):
    __slots__ = ("job_id", "status", "output_file_ids", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: str
    output_file_ids: _containers.RepeatedScalarFieldContainer[str]
    error_message: str
    def __init__(
        self,
        job_id: _Optional[str] = ...,
        status: _Optional[str] = ...,
        output_file_ids: _Optional[_Iterable[str]] = ...,
        error_message: _Optional[str] = ...,
    ) -> None: ...
