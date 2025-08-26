import datetime

from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateData(_message.Message):
    __slots__ = ("name", "context", "template_body", "compiled_at")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_BODY_FIELD_NUMBER: _ClassVar[int]
    COMPILED_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    context: _any_pb2.Any
    template_body: str
    compiled_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., context: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., template_body: _Optional[str] = ..., compiled_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
