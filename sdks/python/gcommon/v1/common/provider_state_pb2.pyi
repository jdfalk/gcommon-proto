from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ProviderState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROVIDER_STATE_UNSPECIFIED: _ClassVar[ProviderState]
    PROVIDER_STATE_CREATING: _ClassVar[ProviderState]
    PROVIDER_STATE_STARTING: _ClassVar[ProviderState]
    PROVIDER_STATE_RUNNING: _ClassVar[ProviderState]
    PROVIDER_STATE_STOPPING: _ClassVar[ProviderState]
    PROVIDER_STATE_STOPPED: _ClassVar[ProviderState]
    PROVIDER_STATE_ERROR: _ClassVar[ProviderState]
    PROVIDER_STATE_UNKNOWN: _ClassVar[ProviderState]

PROVIDER_STATE_UNSPECIFIED: ProviderState
PROVIDER_STATE_CREATING: ProviderState
PROVIDER_STATE_STARTING: ProviderState
PROVIDER_STATE_RUNNING: ProviderState
PROVIDER_STATE_STOPPING: ProviderState
PROVIDER_STATE_STOPPED: ProviderState
PROVIDER_STATE_ERROR: ProviderState
PROVIDER_STATE_UNKNOWN: ProviderState
