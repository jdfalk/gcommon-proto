from gcommon.v1.database import column_metadata_pb2 as _column_metadata_pb2
from gcommon.v1.database import row_pb2 as _row_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultSet(_message.Message):
    __slots__ = ("columns", "rows", "total_count", "has_more")
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedCompositeFieldContainer[
        _column_metadata_pb2.ColumnMetadata
    ]
    rows: _containers.RepeatedCompositeFieldContainer[_row_pb2.Row]
    total_count: int
    has_more: bool
    def __init__(
        self,
        columns: _Optional[
            _Iterable[_Union[_column_metadata_pb2.ColumnMetadata, _Mapping]]
        ] = ...,
        rows: _Optional[_Iterable[_Union[_row_pb2.Row, _Mapping]]] = ...,
        total_count: _Optional[int] = ...,
        has_more: _Optional[bool] = ...,
    ) -> None: ...
