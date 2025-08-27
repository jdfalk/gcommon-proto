from gcommon.v1.queue import cluster_health_pb2 as _cluster_health_pb2
from gcommon.v1.queue import queue_health_pb2 as _queue_health_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetQueueHealthResponse(_message.Message):
    __slots__ = ("queue_health", "cluster_health")
    QUEUE_HEALTH_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_HEALTH_FIELD_NUMBER: _ClassVar[int]
    queue_health: _containers.RepeatedCompositeFieldContainer[
        _queue_health_pb2.QueueHealth
    ]
    cluster_health: _cluster_health_pb2.ClusterHealth
    def __init__(
        self,
        queue_health: _Optional[
            _Iterable[_Union[_queue_health_pb2.QueueHealth, _Mapping]]
        ] = ...,
        cluster_health: _Optional[
            _Union[_cluster_health_pb2.ClusterHealth, _Mapping]
        ] = ...,
    ) -> None: ...
