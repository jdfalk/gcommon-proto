from gcommon.v1.database import query_parameter_pb2 as _query_parameter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseBatchOperation(_message.Message):
    __slots__ = ("statement", "parameters")
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    statement: str
    parameters: _containers.RepeatedCompositeFieldContainer[_query_parameter_pb2.QueryParameter]
    def __init__(self, statement: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_query_parameter_pb2.QueryParameter, _Mapping]]] = ...) -> None: ...
