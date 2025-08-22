from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertSubtitleFormatRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "target_format", "options")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    target_format: str
    options: ConversionOptions
    def __init__(self, subtitle_file_id: _Optional[str] = ..., target_format: _Optional[str] = ..., options: _Optional[_Union[ConversionOptions, _Mapping]] = ...) -> None: ...

class ConversionOptions(_message.Message):
    __slots__ = ("preserve_formatting", "include_metadata", "encoding")
    PRESERVE_FORMATTING_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    preserve_formatting: bool
    include_metadata: bool
    encoding: str
    def __init__(self, preserve_formatting: bool = ..., include_metadata: bool = ..., encoding: _Optional[str] = ...) -> None: ...
