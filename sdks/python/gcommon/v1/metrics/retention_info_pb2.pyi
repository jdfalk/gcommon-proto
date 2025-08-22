from gcommon.v1.metrics import retention_policy_config_pb2 as _retention_policy_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricsRetentionInfo(_message.Message):
    __slots__ = ("total_retained_bytes", "total_purged_bytes", "oldest_data_age", "policies")
    TOTAL_RETAINED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PURGED_BYTES_FIELD_NUMBER: _ClassVar[int]
    OLDEST_DATA_AGE_FIELD_NUMBER: _ClassVar[int]
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    total_retained_bytes: int
    total_purged_bytes: int
    oldest_data_age: str
    policies: _containers.RepeatedCompositeFieldContainer[_retention_policy_config_pb2.RetentionPolicyConfig]
    def __init__(self, total_retained_bytes: _Optional[int] = ..., total_purged_bytes: _Optional[int] = ..., oldest_data_age: _Optional[str] = ..., policies: _Optional[_Iterable[_Union[_retention_policy_config_pb2.RetentionPolicyConfig, _Mapping]]] = ...) -> None: ...
