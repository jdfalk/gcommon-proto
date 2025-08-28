from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportDestinationStats(_message.Message):
    __slots__ = ("destination_id", "destination_type", "exported_metrics", "failed_exports", "success_rate", "last_export")
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_METRICS_FIELD_NUMBER: _ClassVar[int]
    FAILED_EXPORTS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXPORT_FIELD_NUMBER: _ClassVar[int]
    destination_id: str
    destination_type: str
    exported_metrics: int
    failed_exports: int
    success_rate: float
    last_export: _timestamp_pb2.Timestamp
    def __init__(self, destination_id: _Optional[str] = ..., destination_type: _Optional[str] = ..., exported_metrics: _Optional[int] = ..., failed_exports: _Optional[int] = ..., success_rate: _Optional[float] = ..., last_export: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
