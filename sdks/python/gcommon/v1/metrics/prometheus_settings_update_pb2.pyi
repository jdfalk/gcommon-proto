from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrometheusSettingsUpdate(_message.Message):
    __slots__ = ("push_gateway_url", "job_name", "instance", "label_updates", "label_removes")
    class LabelUpdatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PUSH_GATEWAY_URL_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LABEL_UPDATES_FIELD_NUMBER: _ClassVar[int]
    LABEL_REMOVES_FIELD_NUMBER: _ClassVar[int]
    push_gateway_url: str
    job_name: str
    instance: str
    label_updates: _containers.ScalarMap[str, str]
    label_removes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, push_gateway_url: _Optional[str] = ..., job_name: _Optional[str] = ..., instance: _Optional[str] = ..., label_updates: _Optional[_Mapping[str, str]] = ..., label_removes: _Optional[_Iterable[str]] = ...) -> None: ...
