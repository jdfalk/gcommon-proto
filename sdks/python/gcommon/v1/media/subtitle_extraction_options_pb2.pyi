from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SubtitleExtractionOptions(_message.Message):
    __slots__ = ("output_format", "include_hearing_impaired", "include_forced", "languages")
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_HEARING_IMPAIRED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FORCED_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    output_format: str
    include_hearing_impaired: bool
    include_forced: bool
    languages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, output_format: _Optional[str] = ..., include_hearing_impaired: bool = ..., include_forced: bool = ..., languages: _Optional[_Iterable[str]] = ...) -> None: ...
