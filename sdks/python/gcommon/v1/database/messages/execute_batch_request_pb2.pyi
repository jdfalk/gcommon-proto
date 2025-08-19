from gcommon.v1.common.messages import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.database.messages import batch_execute_options_pb2 as _batch_execute_options_pb2
from gcommon.v1.database.messages import batch_operation_pb2 as _batch_operation_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteBatchRequest(_message.Message):
    __slots__ = ("operations", "database", "options", "metadata", "transaction_id")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_batch_operation_pb2.DatabaseBatchOperation]
    database: str
    options: _batch_execute_options_pb2.BatchExecuteOptions
    metadata: _request_metadata_pb2.RequestMetadata
    transaction_id: str
    def __init__(self, operations: _Optional[_Iterable[_Union[_batch_operation_pb2.DatabaseBatchOperation, _Mapping]]] = ..., database: _Optional[str] = ..., options: _Optional[_Union[_batch_execute_options_pb2.BatchExecuteOptions, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ..., transaction_id: _Optional[str] = ...) -> None: ...
