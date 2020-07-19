from typing import overload

import wx


class NonOwnedWindow(wx.Window):
    @overload
    def SetShape(self, region: wx.Region) -> bool: ...
    @overload
    def SetShape(self, path: wx.GraphicsPath) -> bool: ...
