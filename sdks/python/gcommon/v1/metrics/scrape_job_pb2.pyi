from gcommon.v1.metrics import scrape_config_pb2 as _scrape_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScrapeJob(_message.Message):
    __slots__ = ("job_id", "config", "active", "last_scrape_time", "next_scrape_time")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LAST_SCRAPE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_SCRAPE_TIME_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    config: _scrape_config_pb2.ScrapeConfig
    active: bool
    last_scrape_time: _timestamp_pb2.Timestamp
    next_scrape_time: _timestamp_pb2.Timestamp
    def __init__(self, job_id: _Optional[str] = ..., config: _Optional[_Union[_scrape_config_pb2.ScrapeConfig, _Mapping]] = ..., active: bool = ..., last_scrape_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_scrape_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
