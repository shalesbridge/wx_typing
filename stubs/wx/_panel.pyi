from typing import overload, AnyStr, Optional, Text, Union

import wx

class Panel(wx.Window):
    @overload
    def __init__ (self) -> None: ...
    @overload
    def __init__(self, parent: wx.Window, id: wx.WindowID = wx.ID_ANY, pos: wx.Point = wx.DefaultPosition, size: wx.Size = wx.DefaultSize, style: int = 0, name: Union[Text, bytes] = wx.PanelNameStr): ...
    ...
#
# See also
#
# Create
#
#
#
# AcceptsFocus(self)
#
# This method is overridden from wx.Window.AcceptsFocus and returns True only if there is no child window in the panel which can accept the focus.
#
# This is reevaluated each time a child window is added or removed from the panel.
# Return type:	bool
#
#
# Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TAB_TRAVERSAL, name=PanelNameStr)
#
# Used for two-step panel construction.
#
# See wx.Panel for details.
#     Parameters:
#
# parent (wx.Window) –
# id (wx.WindowID) –
# pos (wx.Point) –
# size (wx.Size) –
# style (long) –
# name (string) –
#
# Return type:
#
# bool
#
#
# InitDialog(self)
#
# Sends a wx.InitDialogEvent, which in turn transfers data to the dialog via validators.
#
# See also
#
# wx.InitDialogEvent
#
#
# Layout(self)
#
# See wx.Window.SetAutoLayout : when auto layout is on, this function gets called automatically when the window is resized.
# Return type:	bool
#
#
# SetFocus(self)
#
# Overrides wx.Window.SetFocus .
#
# This method uses the (undocumented) mix-in class ControlContainer which manages the focus and TAB logic for controls which usually have child controls.
#
# In practice, if you call this method and the control has at least one child window, the focus will be given to the child window.
#
# See also
#
# wx.FocusEvent, wx.Window.SetFocus
#
#
# SetFocusIgnoringChildren(self)
#
# In contrast to SetFocus (see above) this will set the focus to the panel even if there are child windows in the panel.
#
# This is only rarely needed.
#
