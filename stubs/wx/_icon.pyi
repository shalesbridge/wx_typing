from typing import overload

import wx


class Icon(wx.GDIObject):

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, icon: wx.Icon) -> None: ...
    @overload
    def __init__(self, name, type: wx.BitmapType = wx.BITMAP_TYPE_ANY, desiredWidth: int = -1, desiredHeight: int = -1) -> None: ...
    @overload
    def __init__(self, loc: wx.IconLocation) -> None: ...
    @overload
    def __init__(self, bmp) -> None: ...

    def CopyFromBitmap(self, bmp: wx.Bitmap) -> None: ...
    # MSW-only: ...
    def CreateFromHICON(self, hicon) -> bool: ...
    def GetDepth(self) -> int: ...
    def GetHandle(self) -> int: ...
    def GetHeight(self) -> int: ...
    def GetWidth(self) -> int: ...
    def IsOk(self) -> bool: ...
    def LoadFile(self, name: wx._WxNameType, type: wx.BitmapType = wx.BITMAP_TYPE_ANY, desiredWidth: int = -1, desiredHeight: int = -1) -> bool: ...
    def SetDepth(self, depth: int) -> None: ...
    def SetHandle(self, handle) -> None: ...  # No description for this in the wxPython API documentation.
    def SetHeight(self, height: int) -> None: ...
    def SetWidth(self, width: int) -> None: ...
    def __bool__(self) -> int: ...
    def __nonzero__(self) -> int: ...


    Depth: int
    Handle: int
    Height: int
    Width: int
