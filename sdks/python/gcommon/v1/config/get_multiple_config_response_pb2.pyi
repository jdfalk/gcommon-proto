from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.config import config_entry_pb2 as _config_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMultipleConfigResponse(_message.Message):
    __slots__ = ("entries", "not_found", "error")
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _config_entry_pb2.ConfigEntry
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_config_entry_pb2.ConfigEntry, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[str, _config_entry_pb2.ConfigEntry]
    not_found: _containers.RepeatedScalarFieldContainer[str]
    error: _error_pb2.Error
    def __init__(self, entries: _Optional[_Mapping[str, _config_entry_pb2.ConfigEntry]] = ..., not_found: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
