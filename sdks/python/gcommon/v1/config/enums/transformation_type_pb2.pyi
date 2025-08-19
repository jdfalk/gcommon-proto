from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TransformationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFORMATION_TYPE_UNSPECIFIED: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_TEMPLATE: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_FUNCTION: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_SCRIPT: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_REGEX: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_JSONPATH: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_XPATH: _ClassVar[TransformationType]
    TRANSFORMATION_TYPE_CUSTOM: _ClassVar[TransformationType]
TRANSFORMATION_TYPE_UNSPECIFIED: TransformationType
TRANSFORMATION_TYPE_TEMPLATE: TransformationType
TRANSFORMATION_TYPE_FUNCTION: TransformationType
TRANSFORMATION_TYPE_SCRIPT: TransformationType
TRANSFORMATION_TYPE_REGEX: TransformationType
TRANSFORMATION_TYPE_JSONPATH: TransformationType
TRANSFORMATION_TYPE_XPATH: TransformationType
TRANSFORMATION_TYPE_CUSTOM: TransformationType
