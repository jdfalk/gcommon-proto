from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChecksumValidation(_message.Message):
    __slots__ = ("passed", "expected_checksum", "actual_checksum", "checksum_algorithm")
    PASSED_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    passed: bool
    expected_checksum: str
    actual_checksum: str
    checksum_algorithm: str
    def __init__(self, passed: bool = ..., expected_checksum: _Optional[str] = ..., actual_checksum: _Optional[str] = ..., checksum_algorithm: _Optional[str] = ...) -> None: ...
