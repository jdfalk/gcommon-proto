from gcommon.v1.common import subject_type_pb2 as _subject_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrantPermissionRequest(_message.Message):
    __slots__ = ("subject_id", "subject_type", "permission_id")
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    subject_id: str
    subject_type: _subject_type_pb2.AuthSubjectType
    permission_id: str
    def __init__(self, subject_id: _Optional[str] = ..., subject_type: _Optional[_Union[_subject_type_pb2.AuthSubjectType, str]] = ..., permission_id: _Optional[str] = ...) -> None: ...
