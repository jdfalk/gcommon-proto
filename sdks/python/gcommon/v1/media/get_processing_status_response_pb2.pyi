import datetime

from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetProcessingStatusResponse(_message.Message):
    __slots__ = (
        "job_id",
        "status",
        "job_type",
        "progress_percent",
        "created_at",
        "updated_at",
        "completed_at",
        "error_message",
        "output_file_ids",
    )
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: str
    job_type: str
    progress_percent: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error_message: str
    output_file_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        job_id: _Optional[str] = ...,
        status: _Optional[str] = ...,
        job_type: _Optional[str] = ...,
        progress_percent: _Optional[int] = ...,
        created_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        updated_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        completed_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        error_message: _Optional[str] = ...,
        output_file_ids: _Optional[_Iterable[str]] = ...,
    ) -> None: ...
