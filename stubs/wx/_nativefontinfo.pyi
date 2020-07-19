from typing import overload, Any, Iterable, Text

import wx

class NativeFontInfo(object):
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, info: wx.NativeFontInfo) -> None:
        ...

    def FromString(self, s: Text) -> bool:
        ...

    def FromUserString(self, s: Text) -> bool:
        ...

    def GetEncoding(self) -> wx.FontEncoding:
        ...

    def GetFaceName(self) -> Text:
        ...

    def GetFamily(self) -> wx.FontFamily:
        ...

    def GetPointSize(self) -> int:
        ...

    def GetStyle(self) -> wx.FontStyle:
        ...

    def GetUnderlined(self) -> bool:
        ...

    def GetWeight(self) -> wx.FontWeight:
        ...

    def Init(self) -> wx.Unknown:
        ...

    def InitFromFont(self, font: wx.Font) -> wx.Unknown:
        ...

    def SetEncoding(self, encoding: wx.FontEncoding):
        ...

    @overload
    def SetFaceName(self, facename: Text) -> bool:
        ...

    @overload
    def SetFaceName(self, facenames: Iterable[Text]) -> wx.Unknown:
        ...

    def SetFamily(self, family: wx.FontFamily) -> wx.Unknown:
        ...

    def SetPointSize(self, pointsize: int) -> wx.Unknown:
        ...

    def SetStyle(self, style: wx.FontStyle) -> wx.Unknown:
        ...

    def SetUnderlined(self, underlined: bool) -> wx.Unknown:
        ...

    def SetWeight(self, weight: wx.FontWeight) -> wx.Unknown:
        ...

    def ToString(self) -> Text:
        ...

    def ToUserString(self) -> Text:
        ...

    def __str__(self) -> Text:
        ...

    Encoding: wx.FontEncoding = ...

    FaceName: Text = ...

    Family: wx.FontFamily = ...

    PointSize: int = ...

    Style: wx.FontStyle = ...

    Underlined: bool = ...

    Weight: wx.FontWeight = ...
