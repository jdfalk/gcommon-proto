from gcommon.v1.common import error_pb2 as _error_pb2
from gcommon.v1.config import config_entry_pb2 as _config_entry_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigResponse(_message.Message):
    __slots__ = ("entry", "found", "error")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    entry: _config_entry_pb2.ConfigEntry
    found: bool
    error: _error_pb2.Error
    def __init__(
        self,
        entry: _Optional[_Union[_config_entry_pb2.ConfigEntry, _Mapping]] = ...,
        found: _Optional[bool] = ...,
        error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...,
    ) -> None: ...
