from gcommon.v1.common import response_metadata_pb2 as _response_metadata_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterCheckResponse(_message.Message):
    __slots__ = ("success", "check_id", "message", "metadata", "warnings")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHECK_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    check_id: str
    message: str
    metadata: _response_metadata_pb2.ResponseMetadata
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, success: bool = ..., check_id: _Optional[str] = ..., message: _Optional[str] = ..., metadata: _Optional[_Union[_response_metadata_pb2.ResponseMetadata, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
