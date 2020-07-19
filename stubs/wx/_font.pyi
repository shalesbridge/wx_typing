from typing import overload, Any, Text

import wx

class Font(wx.GDIObject):
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, font: Font) -> None:
        ...

    @overload
    def __init__(self, fontInfo: wx.FontInfo) -> None:
        ...

    @overload
    def __init__(
        self, pointSize: int, family: wx.FontFamily, style: wx.FontStyle,
        weight: wx.FontWeight, underline: bool = False,
        faceName: Text = "", encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> None:
        ...

    @overload
    def __init__(
        self, pixelSize: wx.Size, family: wx.FontFamily, style: wx.FontStyle,
        weight: wx.FontWeight, underline: bool = False, faceName: Text = "",
        encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> None:
        ...

    @overload
    def __init__(self, nativeInfoString: Text) -> None:
        ...

    @overload
    def __init__(self, nativeInfo: wx.NativeFontInfo) -> None:
        ...

    def Bold(self) -> Font:
        ...

    @staticmethod
    def GetDefaultEncoding() -> wx.FontEncoding:
        ...

    def GetEncoding(self) -> wx.FontEncoding:
        ...

    def GetFaceName(self) -> Text:
        ...

    def GetFamily(self) -> wx.FontFamily:
        ...

    def GetHFONT(self) -> wx.Unknown:
        ...

    def GetNativeFontInfo(self) -> wx.NativeFontInfo:
        ...

    def GetNativeFontInfoDesc(self) ->  Text:
        ...

    def GetNativeFontInfoUserDesc(self) -> Text:
        ...

    def GetPangoFontDescription(self) -> wx.Unknown:
        ...

    def GetPixelSize(self) -> wx.Size:
        ...

    def GetPointSize(self) -> int:
        ...

    def GetStrikethrough(self) -> bool:
        ...

    def GetStyle(self) -> wx.FontStyle:
        ...

    def GetUnderlined(self) -> bool:
        ...

    def GetWeight(self) -> wx.FontWeight:
        ...

    def IsFixedWidth(self) -> bool:
        ...

    def IsOk(self) -> bool:
        ...

    def Italic(self) -> Font:
        ...

    def Larger(self) -> Font:
        ...

    def MakeBold(self) -> Font:
        ...

    def MakeItalic(self) -> Font:
        ...

    def MakeLarger(self) -> Font:
        ...

    def MakeSmaller(self) -> Font:
        ...

    def MakeStrikethrough(self) -> Font:
        ...

    def MakeUnderlined(self) -> Font:
        ...

    @overload
    @staticmethod
    def New(
        pointSize: int, family: wx.FontFamily, style: wx.FontStyle,
        weight: wx.FontWeight, underline: bool = False, faceName: Text = "",
        encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> Font:
        ...

    @overload
    @staticmethod
    def New(
        pointSize: int, family: wx.FontFamily, flags: wx.FontFlag = wx.FONTFLAG_DEFAULT,
        faceName: Text = "", encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> Font:
        ...

    @overload
    @staticmethod
    def New(
        pixelSize: wx.Size, family: wx.FontFamily, style: wx.FontStyle,
        weight: wx.FontWeight, underline: bool = False, faceName: Text = "",
        encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> Font:
        ...

    @overload
    @staticmethod
    def New(
        pixelSize: wx.Size, family: wx.FontFamily,
        flags: wx.FontFlag = wx.FONTFLAG_DEFAULT, faceName: Text = "",
        encoding: wx.FontEncoding = wx.FONTENCODING_DEFAULT
    ) -> Font:
        ...

    @overload
    @staticmethod
    def New(nativeInfo: wx.NativeFontInfo) -> Font:
        ...

    @overload
    @staticmethod
    def New(nativeInfoString: Text) -> Font:
        ...

    def OSXGetCGFont(self) -> wx.Unknown:
        ...

    def Scale(self, x: float) -> Font:
        ...

    def Scaled(self, x: float) -> Font:
        ...

    @staticmethod
    def SetDefaultEncoding(encoding: wx.FontEncoding) -> None:
        ...

    def SetEncoding(self, encoding: wx.FontEncoding) -> None:
        ...

    def SetFaceName(self, faceName: Text) -> bool:
        ...

    def SetFamily(self, family: wx.FontFamily) -> wx.Unknown:
        ...

    @overload
    def SetNativeFontInfo(self, info: Text) -> bool:
        ...

    @overload
    def SetNativeFontInfo(self, info: wx.NativeFontInfo) -> wx.Unknown:
        ...

    def SetNativeFontInfoUserDesc(self, info: Text) -> bool:
        ...

    def SetPixelSize(self, pixelSize: wx.Size) -> wx.Unknown:
        ...

    def SetPointSize(self, pointSize: int) -> wx.Unknown:
        ...

    def SetStrikethrough(self, strikethrough: bool) -> wx.Unknown:
        ...

    def SetStyle(self, style: wx.FontStyle) -> wx.Unknown:
        ...

    def SetSymbolicSize(self, size: wx.FontSymbolicSize) -> wx.Unknown:
        ...

    def SetSymbolicSizeRelativeTo(self, size: wx.FontSymbolicSize, base: int) -> wx.Unknown:
        ...

    def SetUnderlined(self, underlined: bool) -> wx.Unknown:
        ...

    def SetWeight(self, weight: wx.FontWeight) -> wx.Unknown:
        ...

    def Smaller(self) -> Font:
        ...

    def Strikethrough(self) -> Font:
        ...

    def Underlined(self) -> Font:
        ...

    def __bool__(self) -> int:
        ...

    def __nonzero__(self) -> int:
        ...

    # def _copyFrom(self, other)
    #
    # For internal use only.

    # def __ne__(self) -> wx.Unknown:
    #     """Inequality operator.

    #     See reference-counted object comparison for more info.
    #         Parameters:	font (wx.Font) –

    #     """
    #     ...

    # def __eq__(self) -> wx.Unknown:
    #     """Equality operator.

    #     See reference-counted object comparison for more info.
    #         Parameters:	font (wx.Font) –

    #     """
    #     ...


    Encoding: wx.FontEncoding = ...

    FaceName: Text = ...

    Family: wx.FontFamily = ...

    NativeFontInfoDesc: Text = ...

    NativeFontInfoUserDesc: Text = ...

    PixelSize: wx.Size = ...

    PointSize: int = ...

    Style: wx.FontStyle = ...

    Weight: wx.FontWeight = ...

