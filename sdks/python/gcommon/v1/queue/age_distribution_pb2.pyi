from gcommon.v1.queue import age_bucket_pb2 as _age_bucket_pb2
from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgeDistribution(_message.Message):
    __slots__ = ("buckets", "average_age_seconds", "oldest_message_age_seconds")
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    OLDEST_MESSAGE_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[_age_bucket_pb2.AgeBucket]
    average_age_seconds: float
    oldest_message_age_seconds: float
    def __init__(self, buckets: _Optional[_Iterable[_Union[_age_bucket_pb2.AgeBucket, _Mapping]]] = ..., average_age_seconds: _Optional[float] = ..., oldest_message_age_seconds: _Optional[float] = ...) -> None: ...
