import datetime

from gcommon.v1.common import config_change_type_pb2 as _config_change_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateChange(_message.Message):
    __slots__ = ("version", "description", "author", "timestamp", "type", "breaking", "details", "migration_notes")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BREAKING_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_NOTES_FIELD_NUMBER: _ClassVar[int]
    version: str
    description: str
    author: str
    timestamp: _timestamp_pb2.Timestamp
    type: _config_change_type_pb2.TemplateChangeType
    breaking: bool
    details: _containers.RepeatedScalarFieldContainer[str]
    migration_notes: str
    def __init__(self, version: _Optional[str] = ..., description: _Optional[str] = ..., author: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., type: _Optional[_Union[_config_change_type_pb2.TemplateChangeType, str]] = ..., breaking: _Optional[bool] = ..., details: _Optional[_Iterable[str]] = ..., migration_notes: _Optional[str] = ...) -> None: ...
