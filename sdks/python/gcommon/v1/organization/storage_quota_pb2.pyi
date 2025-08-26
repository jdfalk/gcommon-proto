from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StorageQuota(_message.Message):
    __slots__ = ("max_size_bytes", "max_objects", "max_requests_per_second", "transfer_quota_bytes")
    MAX_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUESTS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_QUOTA_BYTES_FIELD_NUMBER: _ClassVar[int]
    max_size_bytes: int
    max_objects: int
    max_requests_per_second: int
    transfer_quota_bytes: int
    def __init__(self, max_size_bytes: _Optional[int] = ..., max_objects: _Optional[int] = ..., max_requests_per_second: _Optional[int] = ..., transfer_quota_bytes: _Optional[int] = ...) -> None: ...
