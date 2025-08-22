from gcommon.v1.config import inheritance_strategy_pb2 as _inheritance_strategy_pb2
from gcommon.v1.config import merge_strategy_pb2 as _merge_strategy_pb2
from gcommon.v1.config import inheritance_filter_pb2 as _inheritance_filter_pb2
from gcommon.v1.config import inheritance_transformation_pb2 as _inheritance_transformation_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InheritanceSettings(_message.Message):
    __slots__ = ("enabled", "strategy", "sources", "filters", "transformations", "merge_values", "merge_strategy", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATIONS_FIELD_NUMBER: _ClassVar[int]
    MERGE_VALUES_FIELD_NUMBER: _ClassVar[int]
    MERGE_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    strategy: _inheritance_strategy_pb2.InheritanceStrategy
    sources: _containers.RepeatedScalarFieldContainer[str]
    filters: _containers.RepeatedCompositeFieldContainer[_inheritance_filter_pb2.InheritanceFilter]
    transformations: _containers.RepeatedCompositeFieldContainer[_inheritance_transformation_pb2.InheritanceTransformation]
    merge_values: bool
    merge_strategy: _merge_strategy_pb2.MergeStrategy
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, enabled: bool = ..., strategy: _Optional[_Union[_inheritance_strategy_pb2.InheritanceStrategy, str]] = ..., sources: _Optional[_Iterable[str]] = ..., filters: _Optional[_Iterable[_Union[_inheritance_filter_pb2.InheritanceFilter, _Mapping]]] = ..., transformations: _Optional[_Iterable[_Union[_inheritance_transformation_pb2.InheritanceTransformation, _Mapping]]] = ..., merge_values: bool = ..., merge_strategy: _Optional[_Union[_merge_strategy_pb2.MergeStrategy, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
