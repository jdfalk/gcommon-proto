from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AcknowledgmentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACKNOWLEDGMENT_MODE_UNSPECIFIED: _ClassVar[AcknowledgmentMode]
    ACKNOWLEDGMENT_MODE_AUTO: _ClassVar[AcknowledgmentMode]
    ACKNOWLEDGMENT_MODE_MANUAL: _ClassVar[AcknowledgmentMode]
    ACKNOWLEDGMENT_MODE_NONE: _ClassVar[AcknowledgmentMode]
ACKNOWLEDGMENT_MODE_UNSPECIFIED: AcknowledgmentMode
ACKNOWLEDGMENT_MODE_AUTO: AcknowledgmentMode
ACKNOWLEDGMENT_MODE_MANUAL: AcknowledgmentMode
ACKNOWLEDGMENT_MODE_NONE: AcknowledgmentMode
