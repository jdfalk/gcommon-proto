from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmailTemplate(_message.Message):
    __slots__ = ("name", "subject", "body_html", "body_text")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    BODY_HTML_FIELD_NUMBER: _ClassVar[int]
    BODY_TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    subject: str
    body_html: str
    body_text: str
    def __init__(self, name: _Optional[str] = ..., subject: _Optional[str] = ..., body_html: _Optional[str] = ..., body_text: _Optional[str] = ...) -> None: ...
