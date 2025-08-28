from gcommon.v1.metrics import exporter_status_pb2 as _exporter_status_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportStatus(_message.Message):
    __slots__ = ("total_exported_metrics", "failed_exports", "last_export", "exporters")
    TOTAL_EXPORTED_METRICS_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXPORT_FIELD_NUMBER: _ClassVar[int]
    EXPORTERS_FIELD_NUMBER: _ClassVar[int]
    total_exported_metrics: int
    failed_exports: int
    last_export: _timestamp_pb2.Timestamp
    exporters: _containers.RepeatedCompositeFieldContainer[_exporter_status_pb2.ExporterStatus]
    def __init__(self, total_exported_metrics: _Optional[int] = ..., failed_exports: _Optional[int] = ..., last_export: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exporters: _Optional[_Iterable[_Union[_exporter_status_pb2.ExporterStatus, _Mapping]]] = ...) -> None: ...
