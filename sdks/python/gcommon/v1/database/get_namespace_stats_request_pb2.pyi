from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetNamespaceStatsRequest(_message.Message):
    __slots__ = ("namespace_id", "include_detailed_metrics", "include_key_distribution")
    NAMESPACE_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DETAILED_METRICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_KEY_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    namespace_id: str
    include_detailed_metrics: bool
    include_key_distribution: bool
    def __init__(self, namespace_id: _Optional[str] = ..., include_detailed_metrics: _Optional[bool] = ..., include_key_distribution: _Optional[bool] = ...) -> None: ...
