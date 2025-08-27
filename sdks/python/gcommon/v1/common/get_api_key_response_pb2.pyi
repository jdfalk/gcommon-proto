from gcommon.v1.common import api_key_pb2 as _api_key_pb2
from gcommon.v1.common import api_key_stats_pb2 as _api_key_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetApiKeyResponse(_message.Message):
    __slots__ = ("api_key", "stats", "error_message")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    api_key: _api_key_pb2.APIKey
    stats: _api_key_stats_pb2.ApiKeyStats
    error_message: str
    def __init__(
        self,
        api_key: _Optional[_Union[_api_key_pb2.APIKey, _Mapping]] = ...,
        stats: _Optional[_Union[_api_key_stats_pb2.ApiKeyStats, _Mapping]] = ...,
        error_message: _Optional[str] = ...,
    ) -> None: ...
