from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MergeSubtitlesResponse(_message.Message):
    __slots__ = ("merged_subtitle_file_id", "statistics", "warnings")
    MERGED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    merged_subtitle_file_id: str
    statistics: MergeStatistics
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, merged_subtitle_file_id: _Optional[str] = ..., statistics: _Optional[_Union[MergeStatistics, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...

class MergeStatistics(_message.Message):
    __slots__ = ("total_entries", "conflicts_resolved", "duplicates_removed")
    TOTAL_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    CONFLICTS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    DUPLICATES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    total_entries: int
    conflicts_resolved: int
    duplicates_removed: int
    def __init__(self, total_entries: _Optional[int] = ..., conflicts_resolved: _Optional[int] = ..., duplicates_removed: _Optional[int] = ...) -> None: ...
