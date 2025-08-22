from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateSubtitlesRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "options")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    options: ValidationOptions
    def __init__(self, subtitle_file_id: _Optional[str] = ..., options: _Optional[_Union[ValidationOptions, _Mapping]] = ...) -> None: ...

class ValidationOptions(_message.Message):
    __slots__ = ("check_timing_overlap", "check_encoding", "check_format_compliance", "check_reading_speed", "max_reading_speed_wpm")
    CHECK_TIMING_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    CHECK_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CHECK_FORMAT_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
    CHECK_READING_SPEED_FIELD_NUMBER: _ClassVar[int]
    MAX_READING_SPEED_WPM_FIELD_NUMBER: _ClassVar[int]
    check_timing_overlap: bool
    check_encoding: bool
    check_format_compliance: bool
    check_reading_speed: bool
    max_reading_speed_wpm: float
    def __init__(self, check_timing_overlap: bool = ..., check_encoding: bool = ..., check_format_compliance: bool = ..., check_reading_speed: bool = ..., max_reading_speed_wpm: _Optional[float] = ...) -> None: ...
