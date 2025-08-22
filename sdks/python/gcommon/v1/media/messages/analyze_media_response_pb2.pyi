from gcommon.v1.media.messages import media_analysis_pb2 as _media_analysis_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeMediaResponse(_message.Message):
    __slots__ = ("job_id", "status", "analysis", "error_message")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: str
    analysis: _media_analysis_pb2.MediaAnalysis
    error_message: str
    def __init__(self, job_id: _Optional[str] = ..., status: _Optional[str] = ..., analysis: _Optional[_Union[_media_analysis_pb2.MediaAnalysis, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...
