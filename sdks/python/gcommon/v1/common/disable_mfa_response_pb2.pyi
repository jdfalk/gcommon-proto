from gcommon.v1.common import mfa_method_pb2 as _mfa_method_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisableMfaResponse(_message.Message):
    __slots__ = ("success", "disabled_methods", "error_message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_METHODS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    disabled_methods: _containers.RepeatedScalarFieldContainer[
        _mfa_method_pb2.MfaMethod
    ]
    error_message: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        disabled_methods: _Optional[
            _Iterable[_Union[_mfa_method_pb2.MfaMethod, str]]
        ] = ...,
        error_message: _Optional[str] = ...,
    ) -> None: ...
