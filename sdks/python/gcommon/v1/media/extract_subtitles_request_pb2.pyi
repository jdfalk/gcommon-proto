from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import subtitle_extraction_options_pb2 as _subtitle_extraction_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractSubtitlesRequest(_message.Message):
    __slots__ = ("media_file_id", "track_indices", "options")
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TRACK_INDICES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    media_file_id: str
    track_indices: _containers.RepeatedScalarFieldContainer[int]
    options: _subtitle_extraction_options_pb2.SubtitleExtractionOptions
    def __init__(self, media_file_id: _Optional[str] = ..., track_indices: _Optional[_Iterable[int]] = ..., options: _Optional[_Union[_subtitle_extraction_options_pb2.SubtitleExtractionOptions, _Mapping]] = ...) -> None: ...
