from gcommon.v1.media import chapter_info_pb2 as _chapter_info_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectChaptersResponse(_message.Message):
    __slots__ = ("chapters", "total_chapters", "confidence_score")
    CHAPTERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHAPTERS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    chapters: _containers.RepeatedCompositeFieldContainer[_chapter_info_pb2.ChapterInfo]
    total_chapters: int
    confidence_score: float
    def __init__(self, chapters: _Optional[_Iterable[_Union[_chapter_info_pb2.ChapterInfo, _Mapping]]] = ..., total_chapters: _Optional[int] = ..., confidence_score: _Optional[float] = ...) -> None: ...
