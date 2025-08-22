from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateSubtitlesResponse(_message.Message):
    __slots__ = ("is_valid", "errors", "warnings", "statistics")
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    errors: _containers.RepeatedCompositeFieldContainer[ValidationError]
    warnings: _containers.RepeatedCompositeFieldContainer[ValidationWarning]
    statistics: ValidationStatistics
    def __init__(self, is_valid: bool = ..., errors: _Optional[_Iterable[_Union[ValidationError, _Mapping]]] = ..., warnings: _Optional[_Iterable[_Union[ValidationWarning, _Mapping]]] = ..., statistics: _Optional[_Union[ValidationStatistics, _Mapping]] = ...) -> None: ...

class ValidationError(_message.Message):
    __slots__ = ("code", "message", "line_number", "severity")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    line_number: int
    severity: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., line_number: _Optional[int] = ..., severity: _Optional[str] = ...) -> None: ...

class ValidationWarning(_message.Message):
    __slots__ = ("code", "message", "line_number")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    line_number: int
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ..., line_number: _Optional[int] = ...) -> None: ...

class ValidationStatistics(_message.Message):
    __slots__ = ("total_entries", "overlapping_entries", "average_reading_speed_wpm", "max_reading_speed_wpm")
    TOTAL_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    OVERLAPPING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_READING_SPEED_WPM_FIELD_NUMBER: _ClassVar[int]
    MAX_READING_SPEED_WPM_FIELD_NUMBER: _ClassVar[int]
    total_entries: int
    overlapping_entries: int
    average_reading_speed_wpm: float
    max_reading_speed_wpm: float
    def __init__(self, total_entries: _Optional[int] = ..., overlapping_entries: _Optional[int] = ..., average_reading_speed_wpm: _Optional[float] = ..., max_reading_speed_wpm: _Optional[float] = ...) -> None: ...
