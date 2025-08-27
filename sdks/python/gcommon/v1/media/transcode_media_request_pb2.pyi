from gcommon.v1.media import transcode_options_pb2 as _transcode_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TranscodeMediaRequest(_message.Message):
    __slots__ = ("media_file_id", "output_format", "output_codec", "options")
    MEDIA_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CODEC_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    media_file_id: str
    output_format: str
    output_codec: str
    options: _transcode_options_pb2.TranscodeOptions
    def __init__(
        self,
        media_file_id: _Optional[str] = ...,
        output_format: _Optional[str] = ...,
        output_codec: _Optional[str] = ...,
        options: _Optional[
            _Union[_transcode_options_pb2.TranscodeOptions, _Mapping]
        ] = ...,
    ) -> None: ...
