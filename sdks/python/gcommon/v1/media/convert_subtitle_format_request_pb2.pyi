from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvertSubtitleFormatRequest(_message.Message):
    __slots__ = ("subtitle_file_id", "target_format", "preserve_styling")
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FORMAT_FIELD_NUMBER: _ClassVar[int]
    PRESERVE_STYLING_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    target_format: str
    preserve_styling: bool
    def __init__(self, subtitle_file_id: _Optional[str] = ..., target_format: _Optional[str] = ..., preserve_styling: bool = ...) -> None: ...
