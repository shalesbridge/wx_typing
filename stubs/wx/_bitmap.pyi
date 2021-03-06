from typing import overload, Any, Optional, Text, Union


import wx

# The wxPython documentation says that "bits" should be "(string) – Specifies an array of pixel values.", but that doesn't seem to make sense...
# TODO: Figure out what "_bitsType" should actually be.
_bitsType = Any

BITMAP_SCREEN_DEPTH: int

class Bitmap(wx.GDIObject):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, bitmap: Bitmap) -> None: ...
    @overload
    def __init__(self, bits: _bitsType, width: int, height: int, depth: int = 1) -> None: ...
    @overload
    def __init__(self, width: int, height: int, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...
    @overload
    def __init__(self, sz: wx.Size, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...
    @overload
    def __init__(self, name: wx._WxNameType, type: wx.BitmapType = wx.BITMAP_TYPE_ANY) -> None: ...
    @overload
    def __init__(self, img: wx.Image, depth: int = BITMAP_SCREEN_DEPTH) -> None: ...

    def ConvertToDisabled(self, brightness: int) -> Bitmap: ...
    def ConvertToImage(self) -> wx.Image: ...
    def CopyFromBuffer(self, data, format: wx.BitmapBufferFormat = wx.BitmapBufferFormat_RGB, stride: int = -1): ...
            #    def BitmapBufferFormat_RGB  A simple sequence of RGB bytes: ...
            #    def BitmapBufferFormat_RGBA  A simple sequence of RGBA bytes: ...
            #    def BitmapBufferFormat_ARGB32  A sequence of 32-bit values in native endian order, with alpha in the upper 8 bits, followed by red, green, and blue.
            #    def BitmapBufferFormat_RGB32  Same as above but the alpha byte is ignored.
    def CopyFromIcon(self, icon: wx.Icon) -> bool: ...
    def CopyToBuffer(self, data, format: wx.BitmapBufferFormat = wx.BitmapBufferFormat_RGB, stride: int = -1) -> wx.Unknown: ...

    @overload
    def Create (self, width: int, height: int, depth: int = BITMAP_SCREEN_DEPTH) -> bool: ...
    @overload
    def Create (self, sz: int, depth: int = BITMAP_SCREEN_DEPTH) -> bool: ...

    @staticmethod
    def FromBuffer(width, height, data) -> Bitmap: ...
    @staticmethod
    def FromBufferAndAlpha(width, height, data, alpha) -> Bitmap: ...
    @staticmethod
    def FromBufferRGBA(width, height, data) -> Bitmap: ...
    @staticmethod
    def FromRGBA(width, height, red=0, green=0, blue=0, alpha=0) -> Bitmap: ...
    def GetDepth(self) -> int: ...
    def GetHandle(self) -> int: ... # MSW-only method to fetch the windows handle for the bitmap.
    def GetHeight(self) -> int: ...
    def GetMask(self) -> wx.Mask: ...
    def GetPalette(self) -> wx.Palette: ...
    def GetSize(self) -> wx.Size: ...
    def GetSubBitmap(self, rect: wx.Rect) -> Bitmap: ...
    def GetWidth(self) -> int: ...
    def IsOk(self) -> bool: ...
    def LoadFile(self, name: wx._WxNameType, type: wx.BitmapType = wx.BITMAP_TYPE_ANY) -> bool: ...
    @staticmethod
    def NewFromPNGData(data, size: int) -> Bitmap: ...
    def SaveFile(self, name: Union[bytes, Text], type: wx.BitmapType, palette: Optional[wx.Palette] = None) -> bool: ...
    def SetDepth(self, depth: int) -> wx.Unknown: ...
    def SetHandle(self) -> wx.Unknown: ...  # MSW-only method to set the windows handle for the bitmap.
    def SetHeight(self, height: int) -> wx.Unknown: ...
    def SetMask(self, mask: wx.Mask) -> wx.Unknown: ...
    def SetMaskColour(self) -> wx.Unknown: ...
    def SetPalette(self, palette: wx.Palette) -> wx.Unknown: ...  # (Not implemented under GTK+).
    def SetSize(self) -> wx.Unknown: ...
    def SetWidth(self, width: int) -> wx.Unknown: ...
    def __bool__(self) -> int: ...
    def __nonzero__(self) -> int: ...

    Depth: int
    Handle: int
    Height: int
    Mask: wx.Mask
    Palette: wx.Palette
    Size: wx.Size
    Width: int
