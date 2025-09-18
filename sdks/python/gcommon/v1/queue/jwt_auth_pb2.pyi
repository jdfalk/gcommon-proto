from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JwtAuth(_message.Message):
    __slots__ = ("enabled", "algorithm", "verification_key", "expected_issuer", "expected_audience", "clock_skew_seconds", "required_claims")
    class RequiredClaimsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_ISSUER_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    CLOCK_SKEW_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CLAIMS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    algorithm: str
    verification_key: str
    expected_issuer: str
    expected_audience: _containers.RepeatedScalarFieldContainer[str]
    clock_skew_seconds: int
    required_claims: _containers.ScalarMap[str, str]
    def __init__(self, enabled: _Optional[bool] = ..., algorithm: _Optional[str] = ..., verification_key: _Optional[str] = ..., expected_issuer: _Optional[str] = ..., expected_audience: _Optional[_Iterable[str]] = ..., clock_skew_seconds: _Optional[int] = ..., required_claims: _Optional[_Mapping[str, str]] = ...) -> None: ...
