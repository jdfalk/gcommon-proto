from gcommon.v1.media import media_file_pb2 as _media_file_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadMediaResponse(_message.Message):
    __slots__ = ("media_file", "upload_id", "success")
    MEDIA_FILE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    media_file: _media_file_pb2.MediaFile
    upload_id: str
    success: bool
    def __init__(
        self,
        media_file: _Optional[_Union[_media_file_pb2.MediaFile, _Mapping]] = ...,
        upload_id: _Optional[str] = ...,
        success: _Optional[bool] = ...,
    ) -> None: ...
