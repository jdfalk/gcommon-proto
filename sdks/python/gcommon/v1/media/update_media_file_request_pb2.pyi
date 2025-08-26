from gcommon.v1.media import media_file_pb2 as _media_file_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateMediaFileRequest(_message.Message):
    __slots__ = ("media_file", "update_mask")
    MEDIA_FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    media_file: _media_file_pb2.MediaFile
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, media_file: _Optional[_Union[_media_file_pb2.MediaFile, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
