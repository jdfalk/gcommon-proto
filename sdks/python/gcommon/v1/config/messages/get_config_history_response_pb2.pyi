from gcommon.v1.metrics.messages import config_change_pb2 as _config_change_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigHistoryResponse(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[_config_change_pb2.MetricsConfigChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[_config_change_pb2.MetricsConfigChange, _Mapping]]] = ...) -> None: ...
