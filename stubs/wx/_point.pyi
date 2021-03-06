from typing import overload, Any, NamedTuple, Tuple

import wx


class Point(object):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: int, y: int) -> None: ...
    @overload
    def __init__ (self, pt: wx.RealPoint) -> None: ...

    def Get(self) -> Tuple[int, int]: ...

    def GetIM(self) -> NamedTuple: ...
    def IsFullySpecified(self) -> bool: ...
    def SetDefaults(self, pt: wx.Point) -> wx.Unknown: ...

    def __getitem__(self, idx: Any) -> bool: ...
    def __len__(self) -> int: ...

    # These seem to be methods that are already defined in the Python type, "object".
    # def __eq__(self, other: Any) -> bool: ...
    # def __ne__(self, other: Any) -> bool ...
    # def __reduce__(self): -> wx.Unknown ...
    # def __repr__(self): -> Text ...
    # def __str__(self): -> Text ...

    def __setitem__(self, idx: Any, val: Any) -> wx.Unknown: ...
    @overload
    def __iadd__(self, sz: wx.Size) -> wx.Unknown: ...
    @overload
    def __iadd__(self, pt: wx.Point) -> wx.Unknown: ...

    @overload
    def __isub__(self, sz: wx.Size) -> wx.Unknown: ...
    @overload
    def __isub__(self, pt: wx.Point) -> wx.Unknown: ...

    IM: NamedTuple
    x: int
    y: int


DefaultPosition: Point = Point(-1, -1)
