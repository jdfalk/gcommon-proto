from gcommon.v1.metrics.messages import retention_policy_pb2 as _retention_policy_pb2
from gcommon.v1.metrics.messages import retention_policy_config_pb2 as _retention_policy_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetentionPolicyInfo(_message.Message):
    __slots__ = ("policy", "config")
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    policy: _retention_policy_pb2.MetricsRetentionPolicy
    config: _retention_policy_config_pb2.RetentionPolicyConfig
    def __init__(self, policy: _Optional[_Union[_retention_policy_pb2.MetricsRetentionPolicy, str]] = ..., config: _Optional[_Union[_retention_policy_config_pb2.RetentionPolicyConfig, _Mapping]] = ...) -> None: ...
