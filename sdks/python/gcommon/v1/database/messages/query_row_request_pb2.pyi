from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.database.messages import query_options_pb2 as _query_options_pb2
from gcommon.v1.database.messages import query_parameter_pb2 as _query_parameter_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryRowRequest(_message.Message):
    __slots__ = ("query", "parameters", "database", "options", "transaction_id", "metadata")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    query: str
    parameters: _containers.RepeatedCompositeFieldContainer[_query_parameter_pb2.QueryParameter]
    database: str
    options: _query_options_pb2.QueryOptions
    transaction_id: str
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, query: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[_query_parameter_pb2.QueryParameter, _Mapping]]] = ..., database: _Optional[str] = ..., options: _Optional[_Union[_query_options_pb2.QueryOptions, _Mapping]] = ..., transaction_id: _Optional[str] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
