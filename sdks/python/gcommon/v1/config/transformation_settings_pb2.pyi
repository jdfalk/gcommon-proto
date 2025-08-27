from gcommon.v1.config import transformation_step_pb2 as _transformation_step_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransformationSettings(_message.Message):
    __slots__ = (
        "enabled",
        "pipeline",
        "transform_on_read",
        "transform_on_write",
        "metadata",
    )
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[str] = ...
        ) -> None: ...

    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ON_READ_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_ON_WRITE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    pipeline: _containers.RepeatedCompositeFieldContainer[
        _transformation_step_pb2.TransformationStep
    ]
    transform_on_read: bool
    transform_on_write: bool
    metadata: _containers.ScalarMap[str, str]
    def __init__(
        self,
        enabled: _Optional[bool] = ...,
        pipeline: _Optional[
            _Iterable[_Union[_transformation_step_pb2.TransformationStep, _Mapping]]
        ] = ...,
        transform_on_read: _Optional[bool] = ...,
        transform_on_write: _Optional[bool] = ...,
        metadata: _Optional[_Mapping[str, str]] = ...,
    ) -> None: ...
