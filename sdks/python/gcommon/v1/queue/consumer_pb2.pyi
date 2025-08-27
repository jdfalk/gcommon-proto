import datetime

from gcommon.v1.common import consumer_state_pb2 as _consumer_state_pb2
from gcommon.v1.queue import consumer_client_pb2 as _consumer_client_pb2
from gcommon.v1.queue import consumer_config_pb2 as _consumer_config_pb2
from gcommon.v1.queue import consumer_stats_pb2 as _consumer_stats_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Consumer(_message.Message):
    __slots__ = (
        "consumer_id",
        "client_info",
        "state",
        "assigned_partitions",
        "config",
        "stats",
        "last_heartbeat",
        "joined_at",
    )
    CONSUMER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    consumer_id: str
    client_info: _consumer_client_pb2.ConsumerClient
    state: _consumer_state_pb2.ConsumerState
    assigned_partitions: _containers.RepeatedScalarFieldContainer[int]
    config: _consumer_config_pb2.ConsumerConfig
    stats: _consumer_stats_pb2.ConsumerStats
    last_heartbeat: _timestamp_pb2.Timestamp
    joined_at: _timestamp_pb2.Timestamp
    def __init__(
        self,
        consumer_id: _Optional[str] = ...,
        client_info: _Optional[
            _Union[_consumer_client_pb2.ConsumerClient, _Mapping]
        ] = ...,
        state: _Optional[_Union[_consumer_state_pb2.ConsumerState, str]] = ...,
        assigned_partitions: _Optional[_Iterable[int]] = ...,
        config: _Optional[_Union[_consumer_config_pb2.ConsumerConfig, _Mapping]] = ...,
        stats: _Optional[_Union[_consumer_stats_pb2.ConsumerStats, _Mapping]] = ...,
        last_heartbeat: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
        joined_at: _Optional[
            _Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]
        ] = ...,
    ) -> None: ...
