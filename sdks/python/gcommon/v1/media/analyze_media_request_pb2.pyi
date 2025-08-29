from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.media import analysis_options_pb2 as _analysis_options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnalyzeMediaRequest(_message.Message):
    __slots__ = ("media_file_id", "options")
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    media_file_id: str
    options: _analysis_options_pb2.AnalysisOptions
    def __init__(self, media_file_id: _Optional[str] = ..., options: _Optional[_Union[_analysis_options_pb2.AnalysisOptions, _Mapping]] = ...) -> None: ...
