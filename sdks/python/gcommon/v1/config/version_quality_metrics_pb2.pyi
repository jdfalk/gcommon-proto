from gcommon.v1.config import version_quality_issue_pb2 as _version_quality_issue_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionQualityMetrics(_message.Message):
    __slots__ = ("quality_score", "test_coverage", "security_score", "performance_score", "complexity_score", "technical_debt_score", "quality_gate_passed", "issues", "timestamp")
    QUALITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    TEST_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    COMPLEXITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_DEBT_SCORE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_GATE_PASSED_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    quality_score: float
    test_coverage: float
    security_score: float
    performance_score: float
    complexity_score: float
    technical_debt_score: float
    quality_gate_passed: bool
    issues: _containers.RepeatedCompositeFieldContainer[_version_quality_issue_pb2.VersionQualityIssue]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, quality_score: _Optional[float] = ..., test_coverage: _Optional[float] = ..., security_score: _Optional[float] = ..., performance_score: _Optional[float] = ..., complexity_score: _Optional[float] = ..., technical_debt_score: _Optional[float] = ..., quality_gate_passed: bool = ..., issues: _Optional[_Iterable[_Union[_version_quality_issue_pb2.VersionQualityIssue, _Mapping]]] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
