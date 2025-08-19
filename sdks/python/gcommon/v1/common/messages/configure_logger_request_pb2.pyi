from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureLoggerRequest(_message.Message):
    __slots__ = ("logger_name", "level", "output_config")
    LOGGER_NAME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    logger_name: str
    level: str
    output_config: str
    def __init__(self, logger_name: _Optional[str] = ..., level: _Optional[str] = ..., output_config: _Optional[str] = ...) -> None: ...
