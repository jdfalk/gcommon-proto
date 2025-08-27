from gcommon.v1.common import filter_operation_pb2 as _filter_operation_pb2
from gcommon.v1.common import int64_array_pb2 as _int64_array_pb2
from gcommon.v1.common import string_array_pb2 as _string_array_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FilterValue(_message.Message):
    __slots__ = (
        "string_value",
        "int_value",
        "double_value",
        "bool_value",
        "string_array",
        "int_array",
        "operation",
    )
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_ARRAY_FIELD_NUMBER: _ClassVar[int]
    INT_ARRAY_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    int_value: int
    double_value: float
    bool_value: bool
    string_array: _string_array_pb2.StringArray
    int_array: _int64_array_pb2.Int64Array
    operation: _filter_operation_pb2.FilterOperation
    def __init__(
        self,
        string_value: _Optional[str] = ...,
        int_value: _Optional[int] = ...,
        double_value: _Optional[float] = ...,
        bool_value: _Optional[bool] = ...,
        string_array: _Optional[_Union[_string_array_pb2.StringArray, _Mapping]] = ...,
        int_array: _Optional[_Union[_int64_array_pb2.Int64Array, _Mapping]] = ...,
        operation: _Optional[_Union[_filter_operation_pb2.FilterOperation, str]] = ...,
    ) -> None: ...
