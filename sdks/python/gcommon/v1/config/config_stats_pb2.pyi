from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigStats(_message.Message):
    __slots__ = (
        "total_configs",
        "active_configs",
        "deprecated_configs",
        "avg_access_frequency",
    )
    TOTAL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    AVG_ACCESS_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    total_configs: int
    active_configs: int
    deprecated_configs: int
    avg_access_frequency: float
    def __init__(
        self,
        total_configs: _Optional[int] = ...,
        active_configs: _Optional[int] = ...,
        deprecated_configs: _Optional[int] = ...,
        avg_access_frequency: _Optional[float] = ...,
    ) -> None: ...
