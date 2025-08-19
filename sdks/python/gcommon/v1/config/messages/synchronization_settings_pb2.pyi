from gcommon.v1.config.enums import conflict_resolution_pb2 as _conflict_resolution_pb2
from gcommon.v1.config.enums import synchronization_frequency_pb2 as _synchronization_frequency_pb2
from gcommon.v1.config.messages import synchronization_target_pb2 as _synchronization_target_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SynchronizationSettings(_message.Message):
    __slots__ = ("enabled", "targets", "frequency", "conflict_resolution", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    targets: _containers.RepeatedCompositeFieldContainer[_synchronization_target_pb2.SynchronizationTarget]
    frequency: _synchronization_frequency_pb2.SynchronizationFrequency
    conflict_resolution: _conflict_resolution_pb2.ConfigConflictResolution
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., targets: _Optional[_Iterable[_Union[_synchronization_target_pb2.SynchronizationTarget, _Mapping]]] = ..., frequency: _Optional[_Union[_synchronization_frequency_pb2.SynchronizationFrequency, str]] = ..., conflict_resolution: _Optional[_Union[_conflict_resolution_pb2.ConfigConflictResolution, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
