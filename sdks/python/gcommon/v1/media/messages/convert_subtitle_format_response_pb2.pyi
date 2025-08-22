from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertSubtitleFormatResponse(_message.Message):
    __slots__ = ("converted_subtitle_file_id", "source_format", "target_format", "warnings")
    CONVERTED_SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FORMAT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    converted_subtitle_file_id: str
    source_format: str
    target_format: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, converted_subtitle_file_id: _Optional[str] = ..., source_format: _Optional[str] = ..., target_format: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
