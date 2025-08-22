from gcommon.v1.common import request_metadata_pb2 as _request_metadata_pb2
from gcommon.v1.common import subscription_preferences_pb2 as _subscription_preferences_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatePreferencesRequest(_message.Message):
    __slots__ = ("preferences", "metadata")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    preferences: _subscription_preferences_pb2.SubscriptionPreferences
    metadata: _request_metadata_pb2.RequestMetadata
    def __init__(self, preferences: _Optional[_Union[_subscription_preferences_pb2.SubscriptionPreferences, _Mapping]] = ..., metadata: _Optional[_Union[_request_metadata_pb2.RequestMetadata, _Mapping]] = ...) -> None: ...
