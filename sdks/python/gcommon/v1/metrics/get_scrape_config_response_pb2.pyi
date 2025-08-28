from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.metrics import scrape_config_pb2 as _scrape_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetScrapeConfigResponse(_message.Message):
    __slots__ = ("config", "error")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    config: _scrape_config_pb2.ScrapeConfig
    error: _error_pb2.Error
    def __init__(self, config: _Optional[_Union[_scrape_config_pb2.ScrapeConfig, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
