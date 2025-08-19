from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics.messages import scrape_config_pb2 as _scrape_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartScrapingRequest(_message.Message):
    __slots__ = ("metadata", "provider_id", "config")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    provider_id: str
    config: _scrape_config_pb2.ScrapeConfig
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., provider_id: _Optional[str] = ..., config: _Optional[_Union[_scrape_config_pb2.ScrapeConfig, _Mapping]] = ...) -> None: ...
