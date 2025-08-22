from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics import unregistration_options_pb2 as _unregistration_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnregisterMetricRequest(_message.Message):
    __slots__ = ("metadata", "metric_name", "metric_id", "provider_id", "options")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    metric_name: str
    metric_id: str
    provider_id: str
    options: _unregistration_options_pb2.UnregistrationOptions
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., metric_name: _Optional[str] = ..., metric_id: _Optional[str] = ..., provider_id: _Optional[str] = ..., options: _Optional[_Union[_unregistration_options_pb2.UnregistrationOptions, _Mapping]] = ...) -> None: ...
