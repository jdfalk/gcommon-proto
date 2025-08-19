from gcommon.v1.queue.messages import dead_letter_queue_config_pb2 as _dead_letter_queue_config_pb2
from gcommon.v1.queue.messages import error_action_config_pb2 as _error_action_config_pb2
from gcommon.v1.queue.messages import error_notification_config_pb2 as _error_notification_config_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorHandlingConfig(_message.Message):
    __slots__ = ("dlq_config", "max_delivery_attempts", "error_actions", "enable_error_logging", "notification_config")
    DLQ_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_DELIVERY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ERROR_LOGGING_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    dlq_config: _dead_letter_queue_config_pb2.DeadLetterQueueConfig
    max_delivery_attempts: int
    error_actions: _containers.RepeatedCompositeFieldContainer[_error_action_config_pb2.ErrorActionConfig]
    enable_error_logging: bool
    notification_config: _error_notification_config_pb2.ErrorNotificationConfig
    def __init__(self, dlq_config: _Optional[_Union[_dead_letter_queue_config_pb2.DeadLetterQueueConfig, _Mapping]] = ..., max_delivery_attempts: _Optional[int] = ..., error_actions: _Optional[_Iterable[_Union[_error_action_config_pb2.ErrorActionConfig, _Mapping]]] = ..., enable_error_logging: bool = ..., notification_config: _Optional[_Union[_error_notification_config_pb2.ErrorNotificationConfig, _Mapping]] = ...) -> None: ...
