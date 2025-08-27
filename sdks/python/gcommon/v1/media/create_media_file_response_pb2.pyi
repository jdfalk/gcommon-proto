from gcommon.v1.media import media_file_pb2 as _media_file_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateMediaFileResponse(_message.Message):
    __slots__ = ("media_file",)
    MEDIA_FILE_FIELD_NUMBER: _ClassVar[int]
    media_file: _media_file_pb2.MediaFile
    def __init__(
        self, media_file: _Optional[_Union[_media_file_pb2.MediaFile, _Mapping]] = ...
    ) -> None: ...
