from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateSubtitlesRequest(_message.Message):
    __slots__ = (
        "subtitle_file_id",
        "check_timing",
        "check_formatting",
        "expected_format",
    )
    SUBTITLE_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    CHECK_TIMING_FIELD_NUMBER: _ClassVar[int]
    CHECK_FORMATTING_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FORMAT_FIELD_NUMBER: _ClassVar[int]
    subtitle_file_id: str
    check_timing: bool
    check_formatting: bool
    expected_format: str
    def __init__(
        self,
        subtitle_file_id: _Optional[str] = ...,
        check_timing: _Optional[bool] = ...,
        check_formatting: _Optional[bool] = ...,
        expected_format: _Optional[str] = ...,
    ) -> None: ...
