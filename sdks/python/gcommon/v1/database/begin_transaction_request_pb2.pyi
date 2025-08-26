from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.database import transaction_options_pb2 as _transaction_options_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BeginTransactionRequest(_message.Message):
    __slots__ = ("database", "options", "metadata")
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    database: str
    options: _transaction_options_pb2.TransactionOptions
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, database: _Optional[str] = ..., options: _Optional[_Union[_transaction_options_pb2.TransactionOptions, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
