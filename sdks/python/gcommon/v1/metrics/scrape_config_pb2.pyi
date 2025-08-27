from gcommon.v1.metrics import scrape_target_pb2 as _scrape_target_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScrapeConfig(_message.Message):
    __slots__ = ("job_name", "targets", "scrape_interval_seconds")
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    SCRAPE_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    job_name: str
    targets: _containers.RepeatedCompositeFieldContainer[
        _scrape_target_pb2.ScrapeTarget
    ]
    scrape_interval_seconds: int
    def __init__(
        self,
        job_name: _Optional[str] = ...,
        targets: _Optional[
            _Iterable[_Union[_scrape_target_pb2.ScrapeTarget, _Mapping]]
        ] = ...,
        scrape_interval_seconds: _Optional[int] = ...,
    ) -> None: ...
