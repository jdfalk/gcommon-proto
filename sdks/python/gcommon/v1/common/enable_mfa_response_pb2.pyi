from gcommon.v1.common import mfa_setup_instruction_pb2 as _mfa_setup_instruction_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnableMfaResponse(_message.Message):
    __slots__ = ("success", "setup_instructions", "error_message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SETUP_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    setup_instructions: _containers.RepeatedCompositeFieldContainer[
        _mfa_setup_instruction_pb2.MfaSetupInstruction
    ]
    error_message: str
    def __init__(
        self,
        success: _Optional[bool] = ...,
        setup_instructions: _Optional[
            _Iterable[_Union[_mfa_setup_instruction_pb2.MfaSetupInstruction, _Mapping]]
        ] = ...,
        error_message: _Optional[str] = ...,
    ) -> None: ...
