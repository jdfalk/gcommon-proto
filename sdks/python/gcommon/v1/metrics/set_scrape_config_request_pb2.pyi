from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import scrape_config_pb2 as _scrape_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetScrapeConfigRequest(_message.Message):
    __slots__ = ("provider_id", "config", "metadata")
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    provider_id: str
    config: _scrape_config_pb2.ScrapeConfig
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, provider_id: _Optional[str] = ..., config: _Optional[_Union[_scrape_config_pb2.ScrapeConfig, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
