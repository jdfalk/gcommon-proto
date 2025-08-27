from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamRestartPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAM_RESTART_POLICY_UNSPECIFIED: _ClassVar[StreamRestartPolicy]
    STREAM_RESTART_POLICY_NEVER: _ClassVar[StreamRestartPolicy]
    STREAM_RESTART_POLICY_IMMEDIATE: _ClassVar[StreamRestartPolicy]
    STREAM_RESTART_POLICY_EXPONENTIAL_BACKOFF: _ClassVar[StreamRestartPolicy]
    STREAM_RESTART_POLICY_FIXED_DELAY: _ClassVar[StreamRestartPolicy]

STREAM_RESTART_POLICY_UNSPECIFIED: StreamRestartPolicy
STREAM_RESTART_POLICY_NEVER: StreamRestartPolicy
STREAM_RESTART_POLICY_IMMEDIATE: StreamRestartPolicy
STREAM_RESTART_POLICY_EXPONENTIAL_BACKOFF: StreamRestartPolicy
STREAM_RESTART_POLICY_FIXED_DELAY: StreamRestartPolicy
