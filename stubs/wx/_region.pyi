from typing import overload, Sequence, Iterable, Iterator

import wx

class Region(Iterable, wx.GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None: ...
    @overload
    def __init__(self, topLeft: wx.Point, bottomRight: wx.Point) -> None: ...
    @overload
    def __init__(self, rect: wx.Rect) -> None: ...
    @overload
    def __init__(self, region: wx.Region) -> None: ...
    @overload
    def __init__(sel, bmp: wx.Bitmap) -> None: ...
    @overload
    def __init__(self, bmp: wx.BitMap, transColour: wx.Colour, tolerance: int = 0) -> None: ...
    @overload
    def __init__(self, points: Sequence, fillStyle: wx.PolygonFillMode = wx.ODDEVEN_RULE) -> None: ...

    def Clear(self, x: int, y: int) -> wx.Unknown: ...

    @overload
    def Contains(self, pt: wx.Point) -> wx.RegionContain: ...
    @overload
    def Contains(self, x: int, y: int, width: int, height: int) -> wx.RegionContain: ...
    @overload
    def Contains(self, rect: wx.Rect) -> wx.RegionContain: ...

    def ConvertToBitmap(self) -> wx.Bitmap: ...

    def GetBox(self) -> wx.Rect: ...

    @overload
    def Intersect(self, x: int, y: int, width: int, height: int) -> bool: ...
    @overload
    def Intersect(self, rect: wx.Rect) -> bool: ...
    @overload
    def Intersect(self, region: Region) -> bool: ...

    def IsEmpty(self) -> bool: ...

    def IsEqual(self, region: Region) -> bool: ...

    @overload
    def Offset(self, x: int, y: int) -> bool: ...
    @overload
    def Offset(self, pt: wx.Point) -> bool: ...


    @overload
    def Subtract(self, rect: wx.Rect) -> bool: ...
    @overload
    def Subtract(self, region: Region) -> bool: ...

    @overload
    def Union(self, x: int, y: int, width: int, height: int) -> bool: ...
    @overload
    def Union(self, rect: wx.Rect) -> 	bool: ...
    @overload
    def Union(self, region: wx.Region) -> 	bool: ...
    @overload
    def Union(self, bmp: wx.Bitmap) -> 	bool: ...
    @overload
    def Union(self, bmp: wx.Bitmap, transColour: wx.Colour, tolerance: int) -> bool: ...

    @overload
    def Xor(self, x: int, y: int, width: int, height: int) -> bool: ...
    @overload
    def Xor(self, rect: wx.Rect) -> bool: ...

    def Xor(self, region: wx.Region) -> bool: ...


    def __iter__(self) -> Iterator: ...

# Properties

    Box: wx.Rect
