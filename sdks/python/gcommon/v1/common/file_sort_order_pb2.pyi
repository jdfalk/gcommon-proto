from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FileSortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_SORT_ORDER_UNSPECIFIED: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_NAME_ASC: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_NAME_DESC: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_SIZE_ASC: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_SIZE_DESC: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_MODIFIED_ASC: _ClassVar[FileSortOrder]
    FILE_SORT_ORDER_MODIFIED_DESC: _ClassVar[FileSortOrder]

FILE_SORT_ORDER_UNSPECIFIED: FileSortOrder
FILE_SORT_ORDER_NAME_ASC: FileSortOrder
FILE_SORT_ORDER_NAME_DESC: FileSortOrder
FILE_SORT_ORDER_SIZE_ASC: FileSortOrder
FILE_SORT_ORDER_SIZE_DESC: FileSortOrder
FILE_SORT_ORDER_MODIFIED_ASC: FileSortOrder
FILE_SORT_ORDER_MODIFIED_DESC: FileSortOrder
