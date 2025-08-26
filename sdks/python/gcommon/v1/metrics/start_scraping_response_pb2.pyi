import datetime

from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import scrape_job_pb2 as _scrape_job_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartScrapingResponse(_message.Message):
    __slots__ = ("success", "error", "job", "started_at")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    JOB_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: _error_pb2.Error
    job: _scrape_job_pb2.ScrapeJob
    started_at: _timestamp_pb2.Timestamp
    def __init__(self, success: _Optional[bool] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., job: _Optional[_Union[_scrape_job_pb2.ScrapeJob, _Mapping]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
