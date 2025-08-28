from gcommon.v1.common import metrics_export_format_pb2 as _metrics_export_format_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportMetricsRequest(_message.Message):
    __slots__ = ("metadata", "provider_id", "format", "destination", "metric_names", "include_metadata")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    METRIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _request_metadata_pb2.RequestMetadata
    provider_id: str
    format: _metrics_export_format_pb2.MetricsExportFormat
    destination: str
    metric_names: _containers.RepeatedScalarFieldContainer[str]
    include_metadata: bool
    def __init__(self, metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., provider_id: _Optional[str] = ..., format: _Optional[_Union[_metrics_export_format_pb2.MetricsExportFormat, str]] = ..., destination: _Optional[str] = ..., metric_names: _Optional[_Iterable[str]] = ..., include_metadata: bool = ...) -> None: ...
