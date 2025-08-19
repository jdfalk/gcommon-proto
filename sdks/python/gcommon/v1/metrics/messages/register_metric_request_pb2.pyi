from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.metrics.messages import metric_definition_pb2 as _metric_definition_pb2
from gcommon.v1.metrics.messages import registration_options_pb2 as _registration_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterMetricRequest(_message.Message):
    __slots__ = ("metadata", "definition", "provider_id", "replace_existing", "options")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    definition: _metric_definition_pb2.MetricDefinition
    provider_id: str
    replace_existing: bool
    options: _registration_options_pb2.RegistrationOptions
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., definition: _Optional[_Union[_metric_definition_pb2.MetricDefinition, _Mapping]] = ..., provider_id: _Optional[str] = ..., replace_existing: bool = ..., options: _Optional[_Union[_registration_options_pb2.RegistrationOptions, _Mapping]] = ...) -> None: ...
