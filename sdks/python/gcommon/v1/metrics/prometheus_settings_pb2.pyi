from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrometheusSettings(_message.Message):
    __slots__ = ("registry", "enable_push_gateway", "push_gateway_url", "job_name", "instance", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REGISTRY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PUSH_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    PUSH_GATEWAY_URL_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    registry: str
    enable_push_gateway: bool
    push_gateway_url: str
    job_name: str
    instance: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, registry: _Optional[str] = ..., enable_push_gateway: bool = ..., push_gateway_url: _Optional[str] = ..., job_name: _Optional[str] = ..., instance: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
