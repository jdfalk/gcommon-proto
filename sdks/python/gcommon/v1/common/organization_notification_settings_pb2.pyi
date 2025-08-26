from gcommon.v1.common import email_template_pb2 as _email_template_pb2
from gcommon.v1.common import notification_frequency_pb2 as _notification_frequency_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrganizationNotificationSettings(_message.Message):
    __slots__ = ("sender_email", "sender_name", "email_enabled", "sms_enabled", "in_app_enabled", "email_templates", "frequency")
    SENDER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SMS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IN_APP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    sender_email: str
    sender_name: str
    email_enabled: bool
    sms_enabled: bool
    in_app_enabled: bool
    email_templates: _containers.RepeatedCompositeFieldContainer[_email_template_pb2.EmailTemplate]
    frequency: _notification_frequency_pb2.NotificationFrequency
    def __init__(self, sender_email: _Optional[str] = ..., sender_name: _Optional[str] = ..., email_enabled: _Optional[bool] = ..., sms_enabled: _Optional[bool] = ..., in_app_enabled: _Optional[bool] = ..., email_templates: _Optional[_Iterable[_Union[_email_template_pb2.EmailTemplate, _Mapping]]] = ..., frequency: _Optional[_Union[_notification_frequency_pb2.NotificationFrequency, _Mapping]] = ...) -> None: ...
