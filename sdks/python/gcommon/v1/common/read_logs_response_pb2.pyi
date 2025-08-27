from gcommon.v1.common import log_entry_pb2 as _log_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadLogsResponse(_message.Message):
    __slots__ = ("entries", "total_count", "error")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[_log_entry_pb2.LogEntry]
    total_count: int
    error: str
    def __init__(
        self,
        entries: _Optional[_Iterable[_Union[_log_entry_pb2.LogEntry, _Mapping]]] = ...,
        total_count: _Optional[int] = ...,
        error: _Optional[str] = ...,
    ) -> None: ...
