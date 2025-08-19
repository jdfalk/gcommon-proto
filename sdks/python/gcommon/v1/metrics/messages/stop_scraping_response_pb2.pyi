from gcommon.v1.common.messages import error_pb2 as _error_pb2
from gcommon.v1.metrics.messages import scrape_job_pb2 as _scrape_job_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StopScrapingResponse(_message.Message):
    __slots__ = ("success", "error", "job", "stopped_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    STOPPED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    job: _scrape_job_pb2.ScrapeJob
    stopped_at: _timestamp_pb2.Timestamp
    def __init__(self, success: bool = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., job: _Optional[_Union[_scrape_job_pb2.ScrapeJob, _Mapping]] = ..., stopped_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
