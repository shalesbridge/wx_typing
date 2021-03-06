from typing import Any, NamedTuple, overload

import wx

class Rect(object):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x : int, y : int, width : int, height : int) -> None: ...
    @overload
    def __init__(self, pos: wx.Point, size: wx.Size) -> None: ...
    @overload
    def __init__(self, size: wx.Size) -> None: ...
    @overload
    def __init__(self, topLeft: wx.Point, bottomRight: wx.Point) -> None: ...

    @overload
    def CenterIn(self, r: Rect, dir: int = wx.BOTH) -> Rect: ...
    @overload
    def CentreIn(self, r: Rect, dir: int = wx.BOTH) -> Rect: ...

    @overload
    def Contains(self, x: int, y: int) -> bool: ...
    @overload
    def Contains(self, pt: wx.Point) -> bool: ...
    @overload
    def Contains(self, rect: Rect) -> bool: ...

    def Deflate(self, dx: int,  dy: int) -> Rect: ...

    @overload
    def Deflate(self, diff: wx.Size) -> Rect: ...
    @overload
    def Deflate(self, diff: int) -> Rect: ...

    def Get(self) -> tuple: ...
    def GetBottom(self) -> int: ...
    def GetBottomLeft(self) -> wx.Point: ...
    def GetBottomRight(self) -> wx.Point: ...
    def GetHeight(self) -> int: ...
    def GetIM(self) -> NamedTuple: ...
    def GetLeft(self) -> int: ...
    def GetPosition(self) -> wx.Point: ...
    def GetRight(self) -> int: ...
    def GetSize(self) -> wx.Size: ...
    def GetTop(self) -> int: ...
    def GetTopLeft(self) -> wx.Point: ...
    def GetTopRight(self) -> wx.Point: ...
    def GetWidth(self) -> int: ...
    def GetX(self) -> int: ...
    def GetY(self) -> int: ...

    @overload
    def Inflate(self, dx: int, dy: int) -> Rect: ...
    @overload
    def Inflate(self, diff: wx.Size) -> Rect: ...
    @overload
    def Inflate(self, diff: int) -> Rect: ...

    def Intersect(self, rect: Rect) -> Rect: ...
    def Intersects(self, rect: Rect) -> bool: ...

    def IsEmpty(self) -> bool: ...

    @overload
    def Offset(self, dx: int, dy: int) -> wx.Unknown: ...
    @overload
    def Offset(self, pt: wx.Point) -> wx.Unknown: ...

    def SetBottom(self, bottom: int) -> wx.Unknown: ...
    def SetBottomLeft(self, p: wx.Point) -> wx.Unknown: ...
    def SetBottomRight(self, p: wx.Point) -> wx.Unknown: ...
    def SetHeight(self, height: int) -> wx.Unknown: ...
    def SetLeft(self, left: int) -> wx.Unknown: ...
    def SetPosition(self, pos: wx.Point) -> wx.Unknown: ...
    def SetRight(self, right: int) -> wx.Unknown: ...
    def SetSize(self, s: wx.Size) -> wx.Unknown: ...
    def SetTop(self, top: int) -> wx.Unknown: ...
    def SetTopLeft(self, p: wx.Point) -> wx.Unknown: ...
    def SetTopRight(self, p: wx.Point) -> wx.Unknown: ...
    def SetWidth(self, width: int) -> wx.Unknown: ...
    def SetX(self, x: int) -> wx.Unknown: ...
    def SetY(self, y: int) -> wx.Unknown: ...
    def Union(self, rect: Rect) -> Rect: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __getitem__(self, idx: Any) -> wx.Unknown: ...
    def __len__(self) -> int: ...

    # __ne__(self, other) -> bool: ...
    # __reduce__(self)
    # __repr__(self)
    # __str__(self)

    def __nonzero__(self) -> wx.Unknown: ...
    def __setitem__(self, idx: Any, val: Any) -> wx.Unknown: ...
    def __imul__(self, r: Rect) -> wx.Unknown: ...
    def __iadd__(self, r: Rect) -> wx.Unknown: ...

    Bottom: int
    BottomLeft: wx.Point
    BottomRight: wx.Point
    Height: int
    Left: int
    Position: wx.Point
    Right: int
    Size: wx.Size
    Top: int
    TopLeft: wx.Point
    TopRight: wx.Point
    Width: int
    X: int
    Y: int
    bottom: int
    bottomLeft: wx.Point
    bottomRight: wx.Point
    height: int
    left: int
    right: int
    top: int
    topLeft: wx.Point
    topRight: wx.Point
    width: int
    x: int
    y: int
