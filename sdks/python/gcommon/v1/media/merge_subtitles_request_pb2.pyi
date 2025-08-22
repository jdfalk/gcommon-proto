from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConflictResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFLICT_RESOLUTION_UNSPECIFIED: _ClassVar[ConflictResolution]
    CONFLICT_RESOLUTION_KEEP_FIRST: _ClassVar[ConflictResolution]
    CONFLICT_RESOLUTION_KEEP_LAST: _ClassVar[ConflictResolution]
    CONFLICT_RESOLUTION_COMBINE: _ClassVar[ConflictResolution]
    CONFLICT_RESOLUTION_ERROR: _ClassVar[ConflictResolution]
CONFLICT_RESOLUTION_UNSPECIFIED: ConflictResolution
CONFLICT_RESOLUTION_KEEP_FIRST: ConflictResolution
CONFLICT_RESOLUTION_KEEP_LAST: ConflictResolution
CONFLICT_RESOLUTION_COMBINE: ConflictResolution
CONFLICT_RESOLUTION_ERROR: ConflictResolution

class MergeSubtitlesRequest(_message.Message):
    __slots__ = ("subtitle_file_ids", "options")
    SUBTITLE_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_ids: _containers.RepeatedScalarFieldContainer[str]
    options: MergeOptions
    def __init__(self, subtitle_file_ids: _Optional[_Iterable[str]] = ..., options: _Optional[_Union[MergeOptions, _Mapping]] = ...) -> None: ...

class MergeOptions(_message.Message):
    __slots__ = ("output_format", "preserve_formatting", "conflict_resolution", "sort_by_timestamp")
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_FORMATTING_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    output_format: str
    preserve_formatting: bool
    conflict_resolution: ConflictResolution
    sort_by_timestamp: bool
    def __init__(self, output_format: _Optional[str] = ..., preserve_formatting: bool = ..., conflict_resolution: _Optional[_Union[ConflictResolution, str]] = ..., sort_by_timestamp: bool = ...) -> None: ...
