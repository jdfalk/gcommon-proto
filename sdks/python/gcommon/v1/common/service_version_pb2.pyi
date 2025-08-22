from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceVersion(_message.Message):
    __slots__ = ("name", "version", "commit", "build_time", "go_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    BUILD_TIME_FIELD_NUMBER: _ClassVar[int]
    GO_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    commit: str
    build_time: _timestamp_pb2.Timestamp
    go_version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., commit: _Optional[str] = ..., build_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., go_version: _Optional[str] = ...) -> None: ...
