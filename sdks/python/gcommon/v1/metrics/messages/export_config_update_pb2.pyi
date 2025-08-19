from gcommon.v1.metrics.messages import export_destination_update_pb2 as _export_destination_update_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExportConfigUpdate(_message.Message):
    __slots__ = ("enabled", "format_updates", "format_removes", "destination_updates", "destination_removes", "frequency", "batch_size")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORMAT_UPDATES_FIELD_NUMBER: _ClassVar[int]
    FORMAT_REMOVES_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_UPDATES_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_REMOVES_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    format_updates: _containers.RepeatedScalarFieldContainer[str]
    format_removes: _containers.RepeatedScalarFieldContainer[str]
    destination_updates: _containers.RepeatedCompositeFieldContainer[_export_destination_update_pb2.ExportDestinationUpdate]
    destination_removes: _containers.RepeatedScalarFieldContainer[str]
    frequency: str
    batch_size: int
    def __init__(self, enabled: bool = ..., format_updates: _Optional[_Iterable[str]] = ..., format_removes: _Optional[_Iterable[str]] = ..., destination_updates: _Optional[_Iterable[_Union[_export_destination_update_pb2.ExportDestinationUpdate, _Mapping]]] = ..., destination_removes: _Optional[_Iterable[str]] = ..., frequency: _Optional[str] = ..., batch_size: _Optional[int] = ...) -> None: ...
