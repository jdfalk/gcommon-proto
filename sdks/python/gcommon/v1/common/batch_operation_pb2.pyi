from buf.validate import validate_pb2 as _validate_pb2
from gcommon.v1.common import batch_options_pb2 as _batch_options_pb2
from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommonBatchOperation(_message.Message):
    __slots__ = ("batch_id", "operation_type", "operations", "options", "metadata")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    operation_type: str
    operations: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    options: _batch_options_pb2.CommonBatchOptions
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(
        self,
        batch_id: _Optional[str] = ...,
        operation_type: _Optional[str] = ...,
        operations: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...,
        options: _Optional[
            _Union[_batch_options_pb2.CommonBatchOptions, _Mapping]
        ] = ...,
        metadata: _Optional[
            _Union[_request_metadata_pb2.RequestMetadata, _Mapping]
        ] = ...,
    ) -> None: ...
