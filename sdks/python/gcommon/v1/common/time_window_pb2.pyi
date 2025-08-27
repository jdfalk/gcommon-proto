from google.protobuf import go_features_pb2 as _go_features_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class TimeWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_WINDOW_UNSPECIFIED: _ClassVar[TimeWindow]
    TIME_WINDOW_1_MINUTE: _ClassVar[TimeWindow]
    TIME_WINDOW_5_MINUTES: _ClassVar[TimeWindow]
    TIME_WINDOW_15_MINUTES: _ClassVar[TimeWindow]
    TIME_WINDOW_30_MINUTES: _ClassVar[TimeWindow]
    TIME_WINDOW_1_HOUR: _ClassVar[TimeWindow]
    TIME_WINDOW_4_HOURS: _ClassVar[TimeWindow]
    TIME_WINDOW_12_HOURS: _ClassVar[TimeWindow]
    TIME_WINDOW_1_DAY: _ClassVar[TimeWindow]
    TIME_WINDOW_1_WEEK: _ClassVar[TimeWindow]
    TIME_WINDOW_1_MONTH: _ClassVar[TimeWindow]
    TIME_WINDOW_1_YEAR: _ClassVar[TimeWindow]
    TIME_WINDOW_CUSTOM: _ClassVar[TimeWindow]

TIME_WINDOW_UNSPECIFIED: TimeWindow
TIME_WINDOW_1_MINUTE: TimeWindow
TIME_WINDOW_5_MINUTES: TimeWindow
TIME_WINDOW_15_MINUTES: TimeWindow
TIME_WINDOW_30_MINUTES: TimeWindow
TIME_WINDOW_1_HOUR: TimeWindow
TIME_WINDOW_4_HOURS: TimeWindow
TIME_WINDOW_12_HOURS: TimeWindow
TIME_WINDOW_1_DAY: TimeWindow
TIME_WINDOW_1_WEEK: TimeWindow
TIME_WINDOW_1_MONTH: TimeWindow
TIME_WINDOW_1_YEAR: TimeWindow
TIME_WINDOW_CUSTOM: TimeWindow
