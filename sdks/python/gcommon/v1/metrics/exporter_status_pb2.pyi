from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExporterStatus(_message.Message):
    __slots__ = ("exporter_id", "exporter_type", "status", "exported_count", "last_export")
    EXPORTER_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXPORTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_EXPORT_FIELD_NUMBER: _ClassVar[int]
    exporter_id: str
    exporter_type: str
    status: str
    exported_count: int
    last_export: _timestamp_pb2.Timestamp
    def __init__(self, exporter_id: _Optional[str] = ..., exporter_type: _Optional[str] = ..., status: _Optional[str] = ..., exported_count: _Optional[int] = ..., last_export: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
