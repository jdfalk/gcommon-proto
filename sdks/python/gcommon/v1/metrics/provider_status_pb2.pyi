import datetime

from gcommon.v1.common import provider_state_pb2 as _provider_state_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderStatus(_message.Message):
    __slots__ = ("state", "message", "health", "last_updated", "version")
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    state: _provider_state_pb2.ProviderState
    message: str
    health: str
    last_updated: _timestamp_pb2.Timestamp
    version: str
    def __init__(
        self,
        state: _Optional[_Union[_provider_state_pb2.ProviderState, str]] = ...,
        message: _Optional[str] = ...,
        health: _Optional[str] = ...,
        last_updated: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        version: _Optional[str] = ...,
    ) -> None: ...
