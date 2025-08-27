from gcommon.v1.common import metrics_config_change_pb2 as _metrics_config_change_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConfigHistoryResponse(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[_metrics_config_change_pb2.MetricsConfigChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[_metrics_config_change_pb2.MetricsConfigChange, _Mapping]]] = ...) -> None: ...
