from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import extracted_subtitle_pb2 as _extracted_subtitle_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractSubtitlesResponse(_message.Message):
    __slots__ = ("job_id", "status", "extracted_subtitles", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRACTED_SUBTITLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: str
    extracted_subtitles: _containers.RepeatedCompositeFieldContainer[_extracted_subtitle_pb2.ExtractedSubtitle]
    error_message: str
    def __init__(self, job_id: _Optional[str] = ..., status: _Optional[str] = ..., extracted_subtitles: _Optional[_Iterable[_Union[_extracted_subtitle_pb2.ExtractedSubtitle, _Mapping]]] = ..., error_message: _Optional[str] = ...) -> None: ...
