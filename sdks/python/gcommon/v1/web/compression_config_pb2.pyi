from gcommon.v1.common import compression_type_pb2 as _compression_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebCompressionConfig(_message.Message):
    __slots__ = ("compression_type", "min_length", "level")
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    compression_type: _compression_type_pb2.LogCompressionType
    min_length: int
    level: int
    def __init__(
        self,
        compression_type: _Optional[
            _Union[_compression_type_pb2.LogCompressionType, str]
        ] = ...,
        min_length: _Optional[int] = ...,
        level: _Optional[int] = ...,
    ) -> None: ...
