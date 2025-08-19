from gcommon.v1.metrics.messages import retention_policy_pb2 as _retention_policy_pb2
from gcommon.v1.queue.enums import priority_level_pb2 as _priority_level_pb2
from gcommon.v1.queue.enums import queue_type_pb2 as _queue_type_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueConfig(_message.Message):
    __slots__ = ("name", "type", "partitions", "retention", "default_priority", "durable", "auto_delete")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    RETENTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DURABLE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _queue_type_pb2.QueueType
    partitions: int
    retention: _retention_policy_pb2.MetricsRetentionPolicy
    default_priority: _priority_level_pb2.PriorityLevel
    durable: bool
    auto_delete: bool
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_queue_type_pb2.QueueType, str]] = ..., partitions: _Optional[int] = ..., retention: _Optional[_Union[_retention_policy_pb2.MetricsRetentionPolicy, str]] = ..., default_priority: _Optional[_Union[_priority_level_pb2.PriorityLevel, str]] = ..., durable: bool = ..., auto_delete: bool = ...) -> None: ...
