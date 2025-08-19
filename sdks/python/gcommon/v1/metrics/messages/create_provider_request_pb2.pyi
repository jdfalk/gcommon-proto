from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics.messages import provider_config_pb2 as _provider_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProviderRequest(_message.Message):
    __slots__ = ("metadata", "config", "validate_config", "dry_run", "auto_start")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    config: _provider_config_pb2.ProviderConfig
    validate_config: bool
    dry_run: bool
    auto_start: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., config: _Optional[_Union[_provider_config_pb2.ProviderConfig, _Mapping]] = ..., validate_config: bool = ..., dry_run: bool = ..., auto_start: bool = ...) -> None: ...
