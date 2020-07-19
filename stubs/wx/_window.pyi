from typing import AnyStr, Text, Union, overload

import wx


# wx.Window is the base class for all windows and represents any visible object on screen.
#
# All controls, top level windows and so on are windows. Sizers and device contexts are not, however, as they don’t appear on screen themselves.
#
# Please note that all children of the window will be deleted automatically by the destructor before the window itself is deleted which means that you don’t have to worry about deleting them manually. Please see the window deletion overview for more information.
#
# Also note that in this, and many others, wxWidgets classes some GetXXX() methods may be overloaded (as, for example, wx.Window.GetSize or wx.Window.GetClientSize ). In this case, the overloads are non-virtual because having multiple virtual functions with the same name results in a virtual function name hiding at the derived class level (in English, this means that the derived class has to override all overloaded variants if it overrides any of them). To allow overriding them in the derived class, wxWidgets uses a unique protected virtual DoGetXXX() method and all GetXXX() ones are forwarded to it, so overriding the former changes the behaviour of the latter.
# styles Window Styles
#
# This class supports the following styles:
#
#     wx.BORDER_DEFAULT: The window class will decide the kind of border to show, if any.
#     wx.BORDER_SIMPLE: Displays a thin border around the window. wx.SIMPLE_BORDER is the old name for this style.
#         wx.BORDER_SUNKEN: Displays a sunken border. wx.SUNKEN_BORDER is the old name for this style.
#         wx.BORDER_RAISED: Displays a raised border. wx.RAISED_BORDER is the old name for this style.
#         wx.BORDER_STATIC: Displays a border suitable for a static control. wx.STATIC_BORDER is the old name for this style. Windows only.
#     wx.BORDER_THEME: Displays a native border suitable for a control, on the current platform. On Windows XP or Vista, this will be a themed border; on most other platforms a sunken border will be used. For more information for themed borders on Windows, please see Themed borders on Windows.
#     wx.BORDER_NONE: Displays no border, overriding the default border style for the window. wx.NO_BORDER is the old name for this style.
#     wx.BORDER_DOUBLE: This style is obsolete and should not be used.
#     wx.TRANSPARENT_WINDOW: The window is transparent, that is, it will not receive paint events. Windows only.
#     wx.TAB_TRAVERSAL: Use this to enable tab traversal for non-dialog windows.
#         wx.WANTS_CHARS: Use this to indicate that the window wants to get all char/key events for all keys - even for keys like TAB or ENTER which are usually used for dialog navigation and which wouldn’t be generated without this style. If you need to use this style in order to get the arrows or etc., but would still like to have normal keyboard navigation take place, you should call Navigate in response to the key events for Tab and Shift-Tab.
#     wx.NO_FULL_REPAINT_ON_RESIZE: On Windows, this style used to disable repainting the window completely when its size is changed. Since this behaviour is now the default, the style is now obsolete and no longer has an effect.
#     wx.VSCROLL: Use this style to enable a vertical scrollbar. Notice that this style cannot be used with native controls which don’t support scrollbars nor with top-level windows in most ports.
#     wx.HSCROLL: Use this style to enable a horizontal scrollbar. The same limitations as for wx.VSCROLL apply to this style.
#     wx.ALWAYS_SHOW_SB: If a window has scrollbars, disable them instead of hiding them when they are not needed (i.e. when the size of the window is big enough to not require the scrollbars to navigate it). This style is currently implemented for wxMSW, wxGTK and wxUniversal and does nothing on the other platforms.
#     wx.CLIP_CHILDREN: Use this style to eliminate flicker caused by the background being repainted, then children being painted over them. Windows only.
#     wx.FULL_REPAINT_ON_RESIZE: Use this style to force a complete redraw of the window whenever it is resized instead of redrawing just the part of the window affected by resizing. Note that this was the behaviour by default before 2.5.1 release and that if you experience redraw problems with code which previously used to work you may want to try this. Currently this style applies on GTK+ 2 and Windows only, and full repainting is always done on other platforms.
#
# extra_styles Window Extra Styles
#
# This class supports the following extra styles:
#
#     wx.WS_EX_VALIDATE_RECURSIVELY: By default, wx.Window.Validate , Window.TransferDataTo() and wx.Window.TransferDataFromWindow only work on direct children of the window (compatible behaviour). Set this flag to make them recursively descend into all subwindows.
#     wx.WS_EX_BLOCK_EVENTS: CommandEvents and the objects of the derived classes are forwarded to the parent window and so on recursively by default. Using this flag for the given window allows to block this propagation at this window, i.e. prevent the events from being propagated further upwards. Dialogs have this flag on by default for the reasons explained in the Events and Event Handling.
#     wx.WS_EX_TRANSIENT: Don’t use this window as an implicit parent for the other windows: this must be used with transient windows as otherwise there is the risk of creating a dialog/frame with this window as a parent, which would lead to a crash if the parent were destroyed before the child.
#     wx.WS_EX_CONTEXTHELP: Under Windows, puts a query button on the caption. When pressed, Windows will go into a context-sensitive help mode and wxWidgets will send a wxEVT_HELP event if the user clicked on an application window. This style cannot be used (because of the underlying native behaviour) together with MAXIMIZE_BOX or MINIMIZE_BOX , so these two styles are automatically turned off if this one is used.
#     wx.WS_EX_PROCESS_IDLE: This window should always process idle events, even if the mode set by wx.IdleEvent.SetMode is IDLE_PROCESS_SPECIFIED .
#     wx.WS_EX_PROCESS_UI_UPDATES: This window should always process UI update events, even if the mode set by wx.UpdateUIEvent.SetMode is UPDATE_UI_PROCESS_SPECIFIED .
#
# events Events Emitted by this Class
#
# Event macros for events emitted by this class:
#
#     EVT_ACTIVATE: Process a wxEVT_ACTIVATE event. See wx.ActivateEvent.
#     EVT_CHILD_FOCUS: Process a wxEVT_CHILD_FOCUS event. See wx.ChildFocusEvent.
#     EVT_CONTEXT_MENU: A right click (or other context menu command depending on platform) has been detected. See wx.ContextMenuEvent.
#     EVT_HELP: Process a wxEVT_HELP event. See wx.HelpEvent.
#     EVT_HELP_RANGE: Process a wxEVT_HELP event for a range of ids. See wx.HelpEvent.
#     EVT_DROP_FILES: Process a wxEVT_DROP_FILES event. See wx.DropFilesEvent.
#     EVT_ERASE_BACKGROUND: Process a wxEVT_ERASE_BACKGROUND event. See wx.EraseEvent.
#     EVT_SET_FOCUS: Process a wxEVT_SET_FOCUS event. See wx.FocusEvent.
#     EVT_KILL_FOCUS: Process a wxEVT_KILL_FOCUS event. See wx.FocusEvent.
#     EVT_IDLE: Process a wxEVT_IDLE event. See wx.IdleEvent.
#     EVT_JOY_*: Processes joystick events. See wx.JoystickEvent.
#     EVT_KEY_DOWN: Process a wxEVT_KEY_DOWN event (any key has been pressed). See wx.KeyEvent.
#     EVT_KEY_UP: Process a wxEVT_KEY_UP event (any key has been released). See wx.KeyEvent.
#     EVT_CHAR: Process a wxEVT_CHAR event. See wx.KeyEvent.
#     EVT_CHAR_HOOK: Process a wxEVT_CHAR_HOOK event. See wx.KeyEvent.
#     EVT_MOUSE_CAPTURE_LOST: Process a wxEVT_MOUSE_CAPTURE_LOST event. See wx.MouseCaptureLostEvent.
#     EVT_MOUSE_CAPTURE_CHANGED: Process a wxEVT_MOUSE_CAPTURE_CHANGED event. See wx.MouseCaptureChangedEvent.
#     EVT_MOUSE_*: See wx.MouseEvent.
#     EVT_PAINT: Process a wxEVT_PAINT event. See wx.PaintEvent.
#     EVT_POWER_*: The system power state changed. See wx.PowerEvent.
#     EVT_SCROLLWIN_*: Process scroll events. See wx.ScrollWinEvent.
#     EVT_SET_CURSOR: Process a wxEVT_SET_CURSOR event. See wx.SetCursorEvent.
#     EVT_SIZE: Process a wxEVT_SIZE event. See wx.SizeEvent.
#     EVT_SYS_COLOUR_CHANGED: Process a wxEVT_SYS_COLOUR_CHANGED event. See wx.SysColourChangedEvent.
#
# See also
#
# Events and Event Handling, Window Sizing Overview
#
# class_hierarchy Class Hierarchy
# Inheritance diagram for class Window:
#

PanelNameStr: bytes = b'panel'


class Window(wx.WindowBase):

    @overload
    def __init__(self): ...
    @overload
    def __init__(self, parent: Window, id: wx.WindowID = wx.ID_ANY, pos: wx.Point = wx.DefaultPosition, size: wx.Size = wx.DefaultSize, style: int = 0, name: Union[Text, bytes] = wx.PanelNameStr) -> None: ...
# AcceptsFocus(self)
#
# This method may be overridden in the derived classes to return False to indicate that this control doesn’t accept input at all (i.e. behaves like e.g. wx.StaticText) and so doesn’t need focus.
# Return type:	bool
#
# See also
#
# AcceptsFocusFromKeyboard
#
#
# AcceptsFocusFromKeyboard(self)
#
# This method may be overridden in the derived classes to return False to indicate that while this control can, in principle, have focus if the user clicks it with the mouse, it shouldn’t be included in the TAB traversal chain when using the keyboard.
# Return type:	bool
#
#
# AcceptsFocusRecursively(self)
#
# Overridden to indicate whether this window or one of its children accepts focus.
#
# Usually it’s the same as AcceptsFocus but is overridden for container windows.
#     Return type:	bool
#
#
# AddChild(self, child)
#
# Adds a child window.
#
# This is called automatically by window creation functions so should not be required by the application programmer. Notice that this function is mostly internal to wxWidgets and shouldn’t be called by the user code.
# Parameters:	child (wx.WindowBase) – Child window to add.
#
#
# AdjustForLayoutDirection(self, x, width, widthTotal)
#
# Mirror coordinates for RTL layout if this window uses it and if the mirroring is not done automatically like Win32.
# Parameters:
#
# x (int) –
# width (int) –
# widthTotal (int) –
#
# Return type:
#
# wx.Coord
#
#
# AlwaysShowScrollbars(self, hflag=True, vflag=True)
#
# Call this function to force one or both scrollbars to be always shown, even if the window is big enough to show its entire contents without scrolling.
# Parameters:
#
# hflag (bool) – Whether the horizontal scroll bar should always be visible.
# vflag (bool) – Whether the vertical scroll bar should always be visible.
#
# New in version 2.9.0.
#
# Note
#
# This function is currently only implemented under Mac/Carbon.
#
#
# AssociateHandle(self, handle)
#
# Associate the window with a new native handle
#
#
# BeginRepositioningChildren(self)
#
# Prepare for changing positions of multiple child windows.
#
# This method should be called before changing positions of multiple child windows to reduce flicker and, in MSW case, even avoid display corruption in some cases. It is used internally by wxWidgets and called automatically when the window size changes but it can also be useful to call it from outside of the library if a repositioning involving multiple children is done without changing the window size.
#
# If this method returns True, then EndRepositioningChildren must be called after setting all children positions. Use wx.Window.ChildrenRepositioningGuard class to ensure that this requirement is satisfied.
# Return type:	bool
#
# New in version 2.9.5.
#
#
# CacheBestSize(self, size)
#
# Sets the cached best size value.
# Parameters:	size (wx.Size) –
#
# See also
#
# GetBestSize
#
#
# CanAcceptFocus(self)
#
# Can this window have focus right now?
#
# If this method returns True, it means that calling SetFocus will put focus either to this window or one of its children, if you need to know whether this window accepts focus itself, use IsFocusable
# Return type:	bool
#
#
# CanAcceptFocusFromKeyboard(self)
#
# Can this window be assigned focus from keyboard right now?
# Return type:	bool
#
#
# CanScroll(self, orient)
#
# Returns True if this window can have a scroll bar in this orientation.
# Parameters:	orient (int) – Orientation to check, either wx.HORIZONTAL or wx.VERTICAL.
# Return type:	bool
#
# New in version 2.9.1.
#
#
# CanSetTransparent(self)
#
# Returns True if the system supports transparent windows and calling SetTransparent may succeed.
#
# If this function returns False, transparent windows are definitely not supported by the current system.
# Return type:	bool
#
#
# CaptureMouse(self)
#
# Directs all mouse input to this window.
#
# Call ReleaseMouse to release the capture.
#
# Note that wxWidgets maintains the stack of windows having captured the mouse and when the mouse is released the capture returns to the window which had had captured it previously and it is only really released if there were no previous window. In particular, this means that you must release the mouse as many times as you capture it, unless the window receives the wx.MouseCaptureLostEvent event.
#
# Any application which captures the mouse in the beginning of some operation must handle wx.MouseCaptureLostEvent and cancel this operation when it receives the event. The event handler must not recapture mouse.
#
# See also
#
# ReleaseMouse , wx.MouseCaptureLostEvent
#
#
# Center(self, dir=BOTH)
#
# A synonym for wx.Centre .
#     Parameters:	dir (int) –
#
#
# CenterOnParent(self, dir=BOTH)
#
# A synonym for CentreOnParent .
#     Parameters:	dir (int) –
#
#
# Centre(self, direction=BOTH)
#
# Centres the window.
# Parameters:	direction (int) – Specifies the direction for the centring. May be wx.HORIZONTAL, wx.VERTICAL or wx.BOTH. It may also include the CENTRE_ON_SCREEN flag if you want to centre the window on the entire screen and not on its parent window.
#
# Note
#
# If the window is a top level one (i.e. doesn’t have a parent), it will be centred relative to the screen anyhow.
#
# See also
#
# wx.Center
#
#
# CentreOnParent(self, direction=BOTH)
#
# Centres the window on its parent.
#
# This is a more readable synonym for wx.Centre .
#     Parameters:	direction (int) – Specifies the direction for the centring. May be wx.HORIZONTAL, wx.VERTICAL or wx.BOTH.
#
# Note
#
# This methods provides for a way to centre top level windows over their parents instead of the entire screen. If there is no parent or if the window is not a top level window, then behaviour is the same as wx.Centre .
#
# See also
#
# wx.TopLevelWindow.CentreOnScreen
#
#
# ClearBackground(self)
#
# Clears the window by filling it with the current background colour.
#
# Does not cause an erase background event to be generated.
#
# Notice that this uses wx.ClientDC to draw on the window and the results of doing it while also drawing on wx.PaintDC for this window are undefined. Hence this method shouldn’t be used from EVT_PAINT handlers, just use wx.DC.Clear on the wx.PaintDC you already use there instead.
#
#
# ClientToScreen(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# ClientToScreen (self, x, y)
#
# Converts to screen coordinates from coordinates relative to this window.
# Parameters:
#
# x (int) – A pointer to a integer value for the x coordinate. Pass the client coordinate in, and a screen coordinate will be passed out.
# y (int) – A pointer to a integer value for the y coordinate. Pass the client coordinate in, and a screen coordinate will be passed out.
#
# Return type:
#
# tuple
#
#
# ClientToScreen (self, pt)
#
# Converts to screen coordinates from coordinates relative to this window.
# Parameters:	pt (wx.Point) – The client position for the second form of the function.
# Return type:	wx.Point
#
#
#
# ClientToWindowSize(self, size)
#
# Converts client area size size to corresponding window size.
#
# In other words, the returned value is what would GetSize return if this window had client area of given size. Components with DefaultCoord value are left unchanged. Note that the conversion is not always exact, it assumes that non-client area doesn’t change and so doesn’t take into account things like menu bar (un)wrapping or (dis)appearance of the scrollbars.
# Parameters:	size (wx.Size) –
# Return type:	wx.Size
#
# New in version 2.8.8.
#
# See also
#
# WindowToClientSize
#
#
# Close(self, force=False)
#
# This function simply generates a wx.CloseEvent whose handler usually tries to close the window.
#
# It doesn’t close the window itself, however.
# Parameters:	force (bool) – False if the window’s close handler should be able to veto the destruction of this window, True if it cannot.
# Return type:	bool
# Returns:	True if the event was handled and not vetoed, False otherwise.
#
# Note
#
# Close calls the close handler for the window, providing an opportunity for the window to choose whether to destroy the window. Usually it is only used with the top level windows ( wx.Frame and wx.Dialog classes) as the others are not supposed to have any special OnClose() logic. The close handler should check whether the window is being deleted forcibly, using wx.CloseEvent.CanVeto , in which case it should destroy the window using wx.Window.Destroy . Note that calling Close does not guarantee that the window will be destroyed; but it provides a way to simulate a manual close of a window, which may or may not be implemented by destroying the window. The default implementation of Dialog.OnCloseWindow does not necessarily delete the dialog, since it will simply simulate an wx.ID_CANCEL event which is handled by the appropriate button event handler and may do anything at all. To guarantee that the window will be destroyed, call wx.Window.Destroy instead
#
# See also
#
# Window Deletion Overview, Destroy , wx.CloseEvent
#
#
# ConvertDialogToPixels(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# ConvertDialogToPixels (self, pt)
#
# Converts a point or size from dialog units to pixels.
#
# For the x dimension, the dialog units are multiplied by the average character width and then divided by 4. For the y dimension, the dialog units are multiplied by the average character height and then divided by 8.
# Parameters:	pt (wx.Point) –
# Return type:	wx.Point
#
# Note
#
# Dialog units are used for maintaining a dialog’s proportions even if the font changes. You can also use these functions programmatically. A convenience macro is defined:
#
# # The C++ convenience macro does not apply for Python, however you can
# # accomplish something similar with a function like this
# def DLG_UNIT(parent, point):
#     return parent.ConvertDialogToPixels(point)
#
# See also
#
# ConvertPixelsToDialog
#
#
# ConvertDialogToPixels (self, sz)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	sz (wx.Size) –
# Return type:	wx.Size
#
#
#
# ConvertPixelsToDialog(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# ConvertPixelsToDialog (self, pt)
#
# Converts a point or size from pixels to dialog units.
#
# For the x dimension, the pixels are multiplied by 4 and then divided by the average character width. For the y dimension, the pixels are multiplied by 8 and then divided by the average character height.
# Parameters:	pt (wx.Point) –
# Return type:	wx.Point
#
# Note
#
# Dialog units are used for maintaining a dialog’s proportions even if the font changes.
#
# See also
#
# ConvertDialogToPixels
#
#
# ConvertPixelsToDialog (self, sz)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	sz (wx.Size) –
# Return type:	wx.Size
#
#
#
# Create(self, parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=0, name=PanelNameStr)
# Parameters:
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
# DLG_UNIT(self, dlg_unit)
#
# A convenience wrapper for ConvertDialogToPixels.
#
#
# Destroy(self)
#
# Destroys the window safely.
#
# Use this function instead of the delete operator, since different window classes can be destroyed differently. Frames and dialogs are not destroyed immediately when this function is called
# Return type:	bool
# Returns:	True if the window has either been successfully deleted, or it has been added to the list of windows pending real deletion.
#
#
# DestroyChildren(self)
#
# Destroys all children of a window.
#
# Called automatically by the destructor.
# Return type:	bool
#
#
# DestroyLater(self)
#
# Schedules the window to be destroyed in the near future.
#
# This should be used whenever Destroy could happen too soon, such as when there may still be events for this window or its children waiting in the event queue.
#
#
# Disable(self)
#
# Disables the window.
#
# Same as Enable Enable(false).
# Return type:	bool
# Returns:	Returns True if the window has been disabled, False if it had been already disabled before the call to this function.
#
#
# DissociateHandle(self)
#
# Dissociate the current native handle from the window
#
#
# DoGetBestClientSize(self)
#
# Override this method to return the best size for a custom control.
#
# A typical implementation of this method should compute the minimal size needed to fully display the control contents taking into account the current font size.
#
# The default implementation simply returns wx.DefaultSize and GetBestSize returns an arbitrary hardcoded size for the window, so you must override it when implementing a custom window class.
#
# Notice that the best size returned by this function is cached internally, so if anything that results in the best size changing (e.g. change to the control contents) happens, you need to call InvalidateBestSize to notify wxWidgets about it.
# Return type:	wx.Size
#
# New in version 2.9.0.
#
# See also
#
# Window Sizing Overview
#
#
# DoGetBestSize(self)
#
# Implementation of GetBestSize that can be overridden.
#
# Notice that it is usually more convenient to override DoGetBestClientSize rather than this method itself as you need to explicitly account for the window borders size if you do the latter.
#
# The default implementation of this function is designed for use in container windows, such as wx.Panel, and works something like this:
#
#     If the window has a sizer then it is used to calculate the best size.
#     Otherwise if the window has layout constraints then those are used to calculate the best size.
#     Otherwise if the window has children then the best size is set to be large enough to show all the children.
#     Otherwise if there are no children then the window’s minimal size will be used as its best size.
#     Otherwise if there is no minimal size set, then the current size is used for the best size.
#
# Return type:	wx.Size
#
# See also
#
# Window Sizing Overview
#
#
# DoUpdateWindowUI(self, event)
#
# Does the window-specific updating after processing the update event.
#
# This function is called by UpdateWindowUI in order to check return values in the wx.UpdateUIEvent and act appropriately. For example, to allow frame and dialog title updating, wxWidgets implements this function as follows:
#
# # do the window-specific processing after processing the update event
# def DoUpdateWindowUI(self, event):
#
#     if event.GetSetEnabled():
#         self.Enable(event.GetEnabled())
#
#     if event.GetSetText():
#
#         if event.GetText() != self.GetTitle():
#             self.SetTitle(event.GetText())
#
# Parameters:	event (wx.UpdateUIEvent) –
#
#
# DragAcceptFiles(self, accept)
#
# Enables or disables eligibility for drop file events (OnDropFiles).
# Parameters:	accept (bool) – If True, the window is eligible for drop file events. If False, the window will not accept drop file events.
#
# Note
#
# Windows only until version 2.8.9, available on all platforms since 2.8.10. Cannot be used together with SetDropTarget on non-Windows platforms.
#
# See also
#
# SetDropTarget
#
#
# Enable(self, enable=True)
#
# Enable or disable the window for user input.
#
# Note that when a parent window is disabled, all of its children are disabled as well and they are reenabled again when the parent is.
# Parameters:	enable (bool) – If True, enables the window for input. If False, disables the window.
# Return type:	bool
# Returns:	Returns True if the window has been enabled or disabled, False if nothing was done, i.e. if the window had already been in the specified state.
#
# See also
#
# IsEnabled , Disable , wx.RadioBox.Enable
#
#
# EndRepositioningChildren(self)
#
# Fix child window positions after setting all of them at once.
#
# This method must be called if and only if the previous call to BeginRepositioningChildren returned True.
#
# New in version 2.9.5.
#
#
# static FindFocus()
#
# Finds the window or control which currently has the keyboard focus.
# Return type:	wx.Window
#
# Note
#
# Note that this is a static function, so it can be called without needing a wx.Window pointer.
#
# See also
#
# SetFocus , HasFocus
#
#
# FindWindow(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# FindWindow (self, id)
#
# Find a child of this window, by id.
#
# May return this if it matches itself.
#
# Notice that only real children, not top level windows using this window as parent, are searched by this function.
# Parameters:	id (long) –
# Return type:	wx.Window
#
#
# FindWindow (self, name)
#
# Find a child of this window, by name.
#
# May return this if it matches itself.
#
# Notice that only real children, not top level windows using this window as parent, are searched by this function.
# Parameters:	name (string) –
# Return type:	wx.Window
#
#
#
# static FindWindowById(id, parent=None)
#
# Find the first window with the given id.
#
# If parent is None, the search will start from all top-level frames and dialog boxes; if not None, the search will be limited to the given window hierarchy. The search is recursive in both cases.
# Parameters:
#
# id (long) –
# parent (wx.Window) –
#
# Return type:
#
# wx.Window
# Returns:
#
# Window with the given id or None if not found.
#
# See also
#
# FindWindow
#
#
# static FindWindowByLabel(label, parent=None)
#
# Find a window by its label.
#
# Depending on the type of window, the label may be a window title or panel item label. If parent is None, the search will start from all top-level frames and dialog boxes; if not None, the search will be limited to the given window hierarchy. The search is recursive in both cases.
# Parameters:
#
# label (string) –
# parent (wx.Window) –
#
# Return type:
#
# wx.Window
# Returns:
#
# Window with the given label or None if not found.
#
# See also
#
# FindWindow
#
#
# static FindWindowByName(name, parent=None)
#
# Find a window by its name (as given in a window constructor or Create function call).
#
# If parent is None, the search will start from all top-level frames and dialog boxes; if not None, the search will be limited to the given window hierarchy.
#
# The search is recursive in both cases. If no window with such name is found, wx.FindWindowByLabel is called.
# Parameters:
#
# name (string) –
# parent (wx.Window) –
#
# Return type:
#
# wx.Window
# Returns:
#
# Window with the given name or None if not found.
#
# See also
#
# FindWindow
#
#
# Fit(self)
#
# Sizes the window so that it fits around its subwindows.
#
# This function won’t do anything if there are no subwindows and will only really work correctly if sizers are used for the subwindows layout.
#
# Also, if the window has exactly one subwindow it is better (faster and the result is more precise as Fit adds some margin to account for fuzziness of its calculations) to call:
#
# window.SetClientSize(child.GetSize())
#
# instead of calling Fit .
#
# See also
#
# Window Sizing Overview
#
#
# FitInside(self)
#
# Similar to Fit , but sizes the interior (virtual) size of a window.
#
# Mainly useful with scrolled windows to reset scrollbars after sizing changes that do not trigger a size event, and/or scrolled windows without an interior sizer. This function similarly won’t do anything if there are no subwindows.
#
#
# Freeze(self)
#
# Freezes the window or, in other words, prevents any updates from taking place on screen, the window is not redrawn at all.
#
# Thaw must be called to reenable window redrawing. Calls to these two functions may be nested but to ensure that the window is properly repainted again, you must thaw it exactly as many times as you froze it.
#
# If the window has any children, they are recursively frozen too.
#
# This method is useful for visual appearance optimization (for example, it is a good idea to use it before doing many large text insertions in a row into a wx.TextCtrl under wxGTK) but is not implemented on all platforms nor for all controls so it is mostly just a hint to wxWidgets and not a mandatory directive.
#
# See also
#
# WindowUpdateLocker , Thaw , IsFrozen
#
#
# GetAcceleratorTable(self)
#
# Gets the accelerator table for this window.
#
# See wx.AcceleratorTable.
# Return type:	wx.AcceleratorTable
#
#
# GetAccessible(self)
#
# Returns the accessible object for this window, if any.
#
# See also wx.Accessible.
# Return type:	wx.Accessible
#
#
# GetAutoLayout(self)
#
# Returns the sizer of which this window is a member, if any, otherwise None.
# Return type:	bool
#
#
# GetBackgroundColour(self)
#
# Returns the background colour of the window.
# Return type:	wx.Colour
#
# See also
#
# SetBackgroundColour , SetForegroundColour , GetForegroundColour
#
#
# GetBackgroundStyle(self)
#
# Returns the background style of the window.
# Return type:	wx.BackgroundStyle
#
# See also
#
# SetBackgroundColour , GetForegroundColour , SetBackgroundStyle , SetTransparent
#
#
# GetBestHeight(self, width)
#
# Returns the best height needed by this window if it had the given width.
# Parameters:	width (int) –
# Return type:	int
#
# New in version 2.9.4.
#
# See also
#
# DoGetBestClientHeight
#
#
# GetBestSize(self)
#
# This functions returns the best acceptable minimal size for the window.
#
# For example, for a static control, it will be the minimal size such that the control label is not truncated. For windows containing subwindows (typically wx.Panel), the size returned by this function will be the same as the size the window would have had after calling Fit .
#
# Override virtual DoGetBestSize or, better, because it’s usually more convenient, DoGetBestClientSize when writing your own custom window class to change the value returned by this public non-virtual method.
#
# Notice that the best size respects the minimal and maximal size explicitly set for the window, if any. So even if some window believes that it needs 200 pixels horizontally, calling SetMaxSize with a width of 100 would ensure that GetBestSize returns the width of at most 100 pixels.
# Return type:	wx.Size
#
# See also
#
# CacheBestSize , Window Sizing Overview
#
#
# GetBestVirtualSize(self)
#
# Return the largest of ClientSize and BestSize (as determined by a sizer, interior children, or other means)
# Return type:	wx.Size
#
#
# GetBestWidth(self, height)
#
# Returns the best width needed by this window if it had the given height.
# Parameters:	height (int) –
# Return type:	int
#
# New in version 2.9.4.
#
# See also
#
# DoGetBestClientWidth
#
#
# GetBorder(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# GetBorder (self, flags)
#
# Get the window border style from the given flags: this is different from simply doing flags wx.BORDER_MASK because it uses GetDefaultBorder() to translate wx.BORDER_DEFAULT to something reasonable.
# Parameters:	flags (long) –
# Return type:	wx.Border
#
#
# GetBorder (self)
#
# Get border for the flags of this window.
# Return type:	wx.Border
#
#
#
# static GetCapture()
#
# Returns the currently captured window.
# Return type:	wx.Window
#
# See also
#
# HasCapture , CaptureMouse , ReleaseMouse , wx.MouseCaptureLostEvent, wx.MouseCaptureChangedEvent
#
#
# GetCaret(self)
#
# Returns the caret() associated with the window.
# Return type:	wx.Caret
#
#
# GetCharHeight(self)
#
# Returns the character height for this window.
#     Return type:	int
#
#
# GetCharWidth(self)
#
# Returns the average character width for this window.
#     Return type:	int
#
#
# GetChildren(self)
#
# Returns a reference to the list of the window’s children.
#
# WindowList is a type-safe List-like class whose elements are of type Window* .
#
# Return type:	WindowList
#
#
# static GetClassDefaultAttributes(variant=WINDOW_VARIANT_NORMAL)
#
# Returns the default font and colours which are used by the control.
#
# This is useful if you want to use the same font or colour in your own control as in a standard control
#
# The variant parameter is only relevant under Mac currently and is ignore under other platforms. Under Mac, it will change the size of the returned font. See SetWindowVariant for more about this.
#
# This static method is “overridden” in many derived classes and so calling, for example, wx.Button.GetClassDefaultAttributes will typically return the values appropriate for a button which will be normally different from those returned by, say, wx.ListCtrl.GetClassDefaultAttributes .
#
# The wx.VisualAttributes structure has at least the fields font , colFg and colBg . All of them may be invalid if it was not possible to determine the default control appearance or, especially for the background colour, if the field doesn’t make sense as is the case for colBg for the controls with themed background.
# Parameters:	variant (WindowVariant) –
# Return type:	wx.VisualAttributes
#
# See also
#
# InheritAttributes
#
#
# GetClientAreaOrigin(self)
#
# Get the origin of the client area of the window relative to the window top left corner (the client area may be shifted because of the borders, scrollbars, other decorations...)
# Return type:	wx.Point
#
#
# GetClientRect(self)
#
# Get the client rectangle in window (i.e. client) coordinates.
# Return type:	wx.Rect
#
#
# GetClientSize(self)
#
# Returns the size of the window ‘client area’ in pixels.
#
# The client area is the area which may be drawn on by the programmer, excluding title bar, border, scrollbars, etc. Note that if this window is a top-level one and it is currently minimized, the return size is empty (both width and height are 0).
#
#
# GetConstraints(self)
#
# Returns a pointer to the window’s layout constraints, or None if there are none.
# Return type:	wx.LayoutConstraints
#
#
# GetContainingSizer(self)
#
# Returns the sizer of which this window is a member, if any, otherwise None.
# Return type:	wx.Sizer
#
#
# GetContentScaleFactor(self)
#
# Returns the magnification of the backing store of this window, eg 2.0 for a window on a retina screen.
# Return type:	float
#
# New in version 2.9.5.
#
#
# GetCursor(self)
#
# Return the cursor associated with this window.
# Return type:	wx.Cursor
#
# See also
#
# wx.SetCursor
#
#
# GetDefaultAttributes(self)
#
# Currently this is the same as calling Window.GetClassDefaultAttributes(wxWindow.GetWindowVariant()).
#
# One advantage of using this function compared to the static version is that the call is automatically dispatched to the correct class (as usual with virtual functions) and you don’t have to specify the class name explicitly.
#
# The other one is that in the future this function could return different results, for example it might return a different font for an “Ok” button than for a generic button if the users GUI is configured to show such buttons in bold font. Of course, the down side is that it is impossible to call this function without actually having an object to apply it to whereas the static version can be used without having to create an object first.
# Return type:	wx.VisualAttributes
#
#
# GetDropTarget(self)
#
# Returns the associated drop target, which may be None.
# Return type:	wx.DropTarget
#
# See also
#
# SetDropTarget , Drag and Drop Overview
#
#
# GetEffectiveMinSize(self)
#
# Merges the window’s best size into the min size and returns the result.
#
# This is the value used by sizers to determine the appropriate amount of space to allocate for the widget.
#
# This is the method called by a wx.Sizer when it queries the size of a window or control.
# Return type:	wx.Size
#
# See also
#
# GetBestSize , SetInitialSize , Window Sizing Overview
#
#
# GetEventHandler(self)
#
# Returns the event handler for this window.
#
# By default, the window is its own event handler.
# Return type:	wx.EvtHandler
#
# See also
#
# SetEventHandler , PushEventHandler , PopEventHandler , wx.EvtHandler.ProcessEvent , wx.EvtHandler
#
#
# GetExtraStyle(self)
#
# Returns the extra style bits for the window.
#     Return type:	long
#
#
# GetFont(self)
#
# Returns the font for this window.
#     Return type:	wx.Font
#
# See also
#
# SetFont
#
#
# GetForegroundColour(self)
#
# Returns the foreground colour of the window.
# Return type:	wx.Colour
#
# Note
#
# The meaning of foreground colour varies according to the window class; it may be the text colour or other colour, or it may not be used at all.
#
# See also
#
# SetForegroundColour , SetBackgroundColour , GetBackgroundColour
#
#
# GetGrandParent(self)
#
# Returns the grandparent of a window, or None if there isn’t one.
# Return type:	wx.Window
#
#
# GetGtkWidget(self)
#
#
# GetHandle(self)
#
# Returns the platform-specific handle of the physical window.
#
# Cast it to an appropriate handle, such as HWND for Windows, Widget for Motif or GtkWidget for GTK.
#
#
# GetHelpText(self)
#
# Gets the help text to be used as context-sensitive help for this window.
#
# Note that the text is actually stored by the current wx.HelpProvider implementation, and not in the window object itself.
# Return type:	string
#
# See also
#
# SetHelpText , GetHelpTextAtPoint , wx.HelpProvider
#
#
# GetHelpTextAtPoint(self, point, origin)
#
# Gets the help text to be used as context-sensitive help for this window.
#
# This method should be overridden if the help message depends on the position inside the window, otherwise GetHelpText can be used.
# Parameters:
#
# point (wx.Point) – Coordinates of the mouse at the moment of help event emission.
# origin (HelpEvent.Origin) – Help event origin, see also wx.HelpEvent.GetOrigin .
#
# Return type:
#
# string
#
#
# GetId(self)
#
# Returns the identifier of the window.
# Return type:	wx.WindowID
#
# Note
#
# Each window has an integer identifier. If the application has not provided one (or the default wx.ID_ANY) a unique identifier with a negative value will be generated.
#
# See also
#
# SetId , Window IDs
#
#
# GetLabel(self)
#
# Generic way of getting a label from any window, for identification purposes.
#     Return type:	string
#
# Note
#
# The interpretation of this function differs from class to class. For frames and dialogs, the value returned is the title. For buttons or static text controls, it is the button text. This function can be useful for meta-programs (such as testing tools or special-needs access programs) which need to identify windows by name.
#
#
# GetLayoutDirection(self)
#
# Returns the layout direction for this window, Note that Layout_Default is returned if layout direction is not supported.
# Return type:	wx.LayoutDirection
#
#
# GetMaxClientSize(self)
#
# Returns the maximum size of window’s client area.
#
# This is an indication to the sizer layout mechanism that this is the maximum possible size as well as the upper bound on window’s size settable using SetClientSize .
# Return type:	wx.Size
#
# See also
#
# GetMaxSize , Window Sizing Overview
#
#
# GetMaxHeight(self)
#
# Returns the vertical component of window maximal size.
#
# The returned value is DefaultCoord if the maximal width was not set.
# Return type:	int
#
# See also
#
# GetMaxSize
#
#
# GetMaxSize(self)
#
# Returns the maximum size of the window.
#
# This is an indication to the sizer layout mechanism that this is the maximum possible size as well as the upper bound on window’s size settable using SetSize .
# Return type:	wx.Size
#
# See also
#
# GetMaxClientSize , Window Sizing Overview
#
#
# GetMaxWidth(self)
#
# Returns the horizontal component of window maximal size.
#
# The returned value is DefaultCoord if the maximal width was not set.
# Return type:	int
#
# See also
#
# GetMaxSize
#
#
# GetMinClientSize(self)
#
# Returns the minimum size of window’s client area, an indication to the sizer layout mechanism that this is the minimum required size of its client area.
#
# It normally just returns the value set by SetMinClientSize , but it can be overridden to do the calculation on demand.
# Return type:	wx.Size
#
# See also
#
# GetMinSize , Window Sizing Overview
#
#
# GetMinHeight(self)
#
# Returns the vertical component of window minimal size.
#
# The returned value is DefaultCoord if the minimal height was not set.
# Return type:	int
#
# See also
#
# GetMinSize
#
#
# GetMinSize(self)
#
# Returns the minimum size of the window, an indication to the sizer layout mechanism that this is the minimum required size.
#
# This method normally just returns the value set by SetMinSize , but it can be overridden to do the calculation on demand.
# Return type:	wx.Size
#
# See also
#
# GetMinClientSize , Window Sizing Overview
#
#
# GetMinWidth(self)
#
# Returns the horizontal component of window minimal size.
#
# The returned value is DefaultCoord if the minimal width was not set.
# Return type:	int
#
# See also
#
# GetMinSize
#
#
# GetName(self)
#
# Returns the window’s name.
# Return type:	string
#
# Note
#
# This name is not guaranteed to be unique; it is up to the programmer to supply an appropriate name in the window constructor or via SetName .
#
# See also
#
# SetName
#
#
# GetNextSibling(self)
#
# Returns the next window after this one among the parent’s children or None if this window is the last child.
# Return type:	wx.Window
#
# New in version 2.8.8.
#
# See also
#
# GetPrevSibling
#
#
# GetParent(self)
#
# Returns the parent of the window, or None if there is no parent.
# Return type:	wx.Window
#
#
# GetPopupMenuSelectionFromUser(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# GetPopupMenuSelectionFromUser (self, menu, pos=DefaultPosition)
#
# This function shows a popup menu at the given position in this window and returns the selected id.
#
# It can be more convenient than the general purpose PopupMenu function for simple menus proposing a choice in a list of strings to the user.
#
# Notice that to avoid unexpected conflicts between the (usually consecutive range of) ids used by the menu passed to this function and the existing EVT_UPDATE_UI() handlers, this function temporarily disables UI updates for the window, so you need to manually disable (or toggle or ...) any items which should be disabled in the menu before showing it.
#
# The parameter menu is the menu to show. The parameter pos (or the parameters x and y) is the position at which to show the menu in client coordinates. It is recommended to not explicitly specify coordinates when calling this method in response to mouse click, because some of the ports (namely, wxGTK) can do a better job of positioning the menu in that case.
# Parameters:
#
# menu (wx.Menu) –
# pos (wx.Point) –
#
# Return type:
#
# int
# Returns:
#
# The selected menu item id or ID_NONE if none selected or an error occurred.
#
# New in version 2.9.0.
#
#
# GetPopupMenuSelectionFromUser (self, menu, x, y)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:
#
# menu (wx.Menu) –
# x (int) –
# y (int) –
#
# Return type:
#
# int
#
#
#
# GetPosition(self)
#
# This gets the position of the window in pixels, relative to the parent window for the child windows or relative to the display origin for the top level windows.
# Return type:	wx.Point
#
# See also
#
# GetScreenPosition
#
#
# GetPrevSibling(self)
#
# Returns the previous window before this one among the parent’s children or
# Return type:	wx.Window
#
# New in version 2.8.8.
#
# See also
#
# GetNextSibling
#
#
# GetRect(self)
#
# Returns the position and size of the window as a wx.Rect object.
# Return type:	wx.Rect
#
# See also
#
# GetScreenRect
#
#
# GetScreenPosition(self)
#
# Returns the window position in screen coordinates, whether the window is a child window or a top level one.
# Return type:	wx.Point
#
# See also
#
# GetPosition
#
#
# GetScreenRect(self)
#
# Returns the position and size of the window on the screen as a wx.Rect object.
# Return type:	wx.Rect
#
# See also
#
# GetRect
#
#
# GetScrollPos(self, orientation)
#
# Returns the built-in scrollbar position.
# Parameters:	orientation (int) –
# Return type:	int
#
# See also
#
# SetScrollbar
#
#
# GetScrollRange(self, orientation)
#
# Returns the built-in scrollbar range.
# Parameters:	orientation (int) –
# Return type:	int
#
# See also
#
# SetScrollbar
#
#
# GetScrollThumb(self, orientation)
#
# Returns the built-in scrollbar thumb size.
# Parameters:	orientation (int) –
# Return type:	int
#
# See also
#
# SetScrollbar
#
#
# GetSize(self)
#
# Returns the size of the entire window in pixels, including title bar, border, scrollbars, etc.
#
# Note that if this window is a top-level one and it is currently minimized, the returned size is the restored window size, not the size of the window icon.
#
# Receives the window width.
#
# Receives the window height.
# Return type:	wx.Size
#
#
# GetSizer(self)
#
# Returns the sizer associated with the window by a previous call to SetSizer , or None.
# Return type:	wx.Sizer
#
#
# GetFullTextExtent(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# GetFullTextExtent (self, string, font=None)
#
# Gets the dimensions of the string as it would be drawn on the window with the currently selected font.
#
# The text extent is returned in the w and h pointers.
# Parameters:
#
# string (string) – String whose extent is to be measured.
# font (wx.Font) – Font to use instead of the current window font (optional).
#
# Return type:
#
# tuple
#
#
# GetFullTextExtent (self, string)
#
# Gets the dimensions of the string as it would be drawn on the window with the currently selected font.
# Parameters:	string (string) –
# Return type:	wx.Size
#
#
#
# GetThemeEnabled(self)
#
# Clears the window by filling it with the current background colour.
#
# Does not cause an erase background event to be generated.
#
# Notice that this uses wx.ClientDC to draw on the window and the results of doing it while also drawing on wx.PaintDC for this window are undefined. Hence this method shouldn’t be used from EVT_PAINT handlers, just use wx.DC.Clear on the wx.PaintDC you already use there instead.
# Return type:	bool
#
#
# GetToolTip(self)
#
# Get the associated tooltip or None if none.
# Return type:	wx.ToolTip
#
#
# GetToolTipText(self)
#
# Get the text of the associated tooltip or empty string if none.
# Return type:	string
#
#
# GetTopLevelParent(self)
#
# Returns the first ancestor of this window which is a top-level window.
# Return type:	wx.Window
#
#
# GetUpdateClientRect(self)
#
# Get the update rectangle bounding box in client coords.
# Return type:	wx.Rect
#
#
# GetUpdateRegion(self)
#
# Returns the region specifying which parts of the window have been damaged.
#
# Should only be called within an wx.PaintEvent handler.
# Return type:	wx.Region
#
# See also
#
# wx.Region, wx.RegionIterator
#
#
# GetValidator(self)
#
# Validator functions.
#
# Returns a pointer to the current validator for the window, or None if there is none.
# Return type:	wx.Validator
#
#
# GetVirtualSize(self)
#
# This gets the virtual size of the window in pixels.
#
# By default it returns the client size of the window, but after a call to SetVirtualSize it will return the size set with that method.
# Return type:	wx.Size
#
# See also
#
# Window Sizing Overview
#
#
# GetWindowBorderSize(self)
#
# Returns the size of the left/right and top/bottom borders of this window in x and y components of the result respectively.
# Return type:	wx.Size
#
#
# GetWindowStyle(self)
#
# See GetWindowStyleFlag for more info.
#     Return type:	long
#
#
# GetWindowStyleFlag(self)
#
# Gets the window style that was passed to the constructor or Create method.
#
# GetWindowStyle is another name for the same function.
# Return type:	long
#
#
# GetWindowVariant(self)
#
# Returns the value previously passed to SetWindowVariant .
# Return type:	wx.WindowVariant
#
#
# HandleAsNavigationKey(self, event)
#
# This function will generate the appropriate call to Navigate if the key event is one normally used for keyboard navigation and return True in this case.
# Parameters:	event (wx.KeyEvent) –
# Return type:	bool
# Returns:	Returns True if the key pressed was for navigation and was handled, False otherwise.
#
# See also
#
# Navigate
#
#
# HandleWindowEvent(self, event)
#
# Shorthand for:
#
# GetEventHandler().SafelyProcessEvent(event)
#
# Parameters:	event (wx.Event) –
# Return type:	bool
#
# See also
#
# ProcessWindowEvent
#
#
# HasCapture(self)
#
# Returns True if this window has the current mouse capture.
# Return type:	bool
#
# See also
#
# CaptureMouse , ReleaseMouse , wx.MouseCaptureLostEvent, wx.MouseCaptureChangedEvent
#
#
# HasExtraStyle(self, exFlag)
#
# Returns True if the window has the given exFlag bit set in its extra styles.
# Parameters:	exFlag (int) –
# Return type:	bool
#
# See also
#
# SetExtraStyle
#
#
# HasFlag(self, flag)
#
# Returns True if the window has the given flag bit set.
# Parameters:	flag (int) –
# Return type:	bool
#
#
# HasFocus(self)
#
# Returns True if the window (or in case of composite controls, its main child window) has focus.
# Return type:	bool
#
# New in version 2.9.0.
#
# See also
#
# FindFocus
#
#
# HasMultiplePages(self)
#
# This method should be overridden to return True if this window has multiple pages.
#
# All standard class with multiple pages such as wx.Notebook, wx.Listbook and wx.Treebook already override it to return True and user-defined classes with similar behaviour should also do so, to allow the library to handle such windows appropriately.
# Return type:	bool
#
#
# HasScrollbar(self, orient)
#
# Returns True if this window currently has a scroll bar for this orientation.
#
# This method may return False even when CanScroll for the same orientation returns True, but if CanScroll returns False, i.e. scrolling in this direction is not enabled at all, HasScrollbar always returns False as well.
# Parameters:	orient (int) – Orientation to check, either wx.HORIZONTAL or wx.VERTICAL.
# Return type:	bool
#
#
# HasTransparentBackground(self)
#
# Returns True if this window background is transparent (as, for example, for wx.StaticText) and should show the parent window background.
#
# This method is mostly used internally by the library itself and you normally shouldn’t have to call it. You may, however, have to override it in your Window-derived class to ensure that background is painted correctly.
# Return type:	bool
#
#
# Hide(self)
#
# Equivalent to calling wx.Window.Show (False).
# Return type:	bool
#
#
# HideWithEffect(self, effect, timeout=0)
#
# This function hides a window, like Hide , but using a special visual effect if possible.
#
# The parameters of this function are the same as for ShowWithEffect , please see their description there.
# Parameters:
#
# effect (ShowEffect) –
# timeout (int) –
#
# Return type:
#
# bool
#
# New in version 2.9.0.
#
#
# HitTest(self, *args, **kw)
#
# Get the window border style from the given flags: this is different from simply doing flags wx.BORDER_MASK because it uses GetDefaultBorder() to translate wx.BORDER_DEFAULT to something reasonable.
#
# overload Overloaded Implementations:
#
#
# HitTest (self, x, y)
# Parameters:
#
# x (int) –
# y (int) –
#
# Return type:
#
# wx.HitTest
#
#
# HitTest (self, pt)
# Parameters:	pt (wx.Point) –
# Return type:	wx.HitTest
#
#
#
# InformFirstDirection(self, direction, size, availableOtherDir)
#
# wx.Sizer and friends use this to give a chance to a component to recalc its min size once one of the final size components is known.
#
# Override this function when that is useful (such as for wx.StaticText which can stretch over several lines). Parameter availableOtherDir tells the item how much more space there is available in the opposite direction (-1 if unknown).
# Parameters:
#
# direction (int) –
# size (int) –
# availableOtherDir (int) –
#
# Return type:
#
# bool
#
#
# InheritAttributes(self)
#
# This function is (or should be, in case of custom controls) called during window creation to intelligently set up the window visual attributes, that is the font and the foreground and background colours.
#
# By “intelligently” the following is meant: by default, all windows use their own GetClassDefaultAttributes default attributes. However if some of the parents attributes are explicitly (that is, using SetFont and not wx.Window.SetOwnFont ) changed and if the corresponding attribute hadn’t been explicitly set for this window itself, then this window takes the same value as used by the parent. In addition, if the window overrides ShouldInheritColours to return False, the colours will not be changed no matter what and only the font might.
#
# This rather complicated logic is necessary in order to accommodate the different usage scenarios. The most common one is when all default attributes are used and in this case, nothing should be inherited as in modern GUIs different controls use different fonts (and colours) than their siblings so they can’t inherit the same value from the parent. However it was also deemed desirable to allow to simply change the attributes of all children at once by just changing the font or colour of their common parent, hence in this case we do inherit the parents attributes.
#
#
# InheritsBackgroundColour(self)
#
# Return True if this window inherits the background colour from its parent.
# Return type:	bool
#
# See also
#
# SetOwnBackgroundColour , InheritAttributes
#
#
# InitDialog(self)
#
# Sends an wxEVT_INIT_DIALOG event, whose handler usually transfers data to the dialog via validators.
#
#
# InvalidateBestSize(self)
#
# Resets the cached best size value so it will be recalculated the next time it is needed.
#
# See also
#
# CacheBestSize
#
#
# IsBeingDeleted(self)
#
# Returns True if this window is in process of being destroyed.
#
# Top level windows are not deleted immediately but are rather scheduled for later destruction to give them time to process any pending messages; see Destroy description.
#
# This function returns True if this window, or one of its parent windows, is scheduled for destruction and can be useful to avoid manipulating it as it’s usually useless to do something with a window which is on the point of disappearing anyhow.
# Return type:	bool
#
#
# IsDescendant(self, win)
#
# Check if the specified window is a descendant of this one.
#
# Returns True if the window is a descendant (i.e. a child or grand-child or grand-grand-child or ...) of this one.
#
# Notice that a window can never be a descendant of another one if they are in different top level windows, i.e. a child of a wx.Dialog is not considered to be a descendant of dialogs parent wx.Frame.
# Parameters:	win (wx.WindowBase) – Any window, possible None (False is always returned then).
# Return type:	bool
#
# New in version 2.9.4.
#
#
# IsDoubleBuffered(self)
#
# Returns True if the window contents is double-buffered by the system, i.e. if any drawing done on the window is really done on a temporary backing surface and transferred to the screen all at once later.
# Return type:	bool
#
# See also
#
# wx.BufferedDC
#
#
# IsEnabled(self)
#
# Returns True if the window is enabled, i.e. if it accepts user input, False otherwise.
#
# Notice that this method can return False even if this window itself hadn’t been explicitly disabled when one of its parent windows is disabled. To get the intrinsic status of this window, use IsThisEnabled
# Return type:	bool
#
# See also
#
# Enable
#
#
# IsExposed(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# IsExposed (self, x, y)
#
# Returns True if the given point or rectangle area has been exposed since the last repaint.
#
# Call this in an paint event handler to optimize redrawing by only redrawing those areas, which have been exposed.
# Parameters:
#
# x (int) –
# y (int) –
#
# Return type:
#
# bool
#
#
# IsExposed (self, pt)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	pt (wx.Point) –
# Return type:	bool
#
#
# IsExposed (self, x, y, w, h)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:
#
# x (int) –
# y (int) –
# w (int) –
# h (int) –
#
# Return type:
#
# bool
#
#
# IsExposed (self, rect)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	rect (wx.Rect) –
# Return type:	bool
#
#
#
# IsFocusable(self)
#
# Can this window itself have focus?
# Return type:	bool
#
#
# IsFrozen(self)
#
# Returns True if the window is currently frozen by a call to Freeze .
# Return type:	bool
#
# See also
#
# Freeze , Thaw
#
#
# IsRetained(self)
#
# Returns True if the window is retained, False otherwise.
# Return type:	bool
#
# Note
#
# Retained windows are only available on X platforms.
#
#
# IsScrollbarAlwaysShown(self, orient)
#
# Return whether a scrollbar is always shown.
# Parameters:	orient (int) – Orientation to check, either wx.HORIZONTAL or wx.VERTICAL.
# Return type:	bool
#
# See also
#
# AlwaysShowScrollbars
#
#
# IsShown(self)
#
# Returns True if the window is shown, False if it has been hidden.
# Return type:	bool
#
# See also
#
# IsShownOnScreen
#
#
# IsShownOnScreen(self)
#
# Returns True if the window is physically visible on the screen, i.e. it is shown and all its parents up to the toplevel window are shown as well.
# Return type:	bool
#
# See also
#
# IsShown
#
#
# IsThisEnabled(self)
#
# Returns True if this window is intrinsically enabled, False otherwise, i.e. if Enable Enable(false) had been called.
#
# This method is mostly used for wxWidgets itself, user code should normally use IsEnabled instead.
# Return type:	bool
#
#
# IsTopLevel(self)
#
# Returns True if the given window is a top-level one.
#
# Currently all frames and dialogs are considered to be top-level windows (even if they have a parent window).
# Return type:	bool
#
#
# IsTransparentBackgroundSupported(self, reason=None)
#
# Checks whether using transparent background might work.
#
# If this function returns False, calling SetBackgroundStyle with BG_STYLE_TRANSPARENT is not going to work. If it returns True, setting transparent style should normally succeed.
#
# Notice that this function would typically be called on the parent of a window you want to set transparent background style for as the window for which this method is called must be fully created.
# Parameters:	reason (string) – If not None, a reason message is provided if transparency is not supported.
# Return type:	bool
# Returns:	True if background transparency is supported.
#
# New in version 2.9.4.
#
#
# Layout(self)
#
# Invokes the constraint-based layout algorithm or the sizer-based algorithm for this window.
#
# This function does not get called automatically when the window is resized because lots of windows deriving from wx.Window does not need this functionality. If you want to have Layout called automatically, you should derive from wx.Panel (see wx.Panel.Layout ).
# Return type:	bool
#
# See also
#
# Window Sizing Overview
#
#
# LineDown(self)
#
# Same as ScrollLines (1).
# Return type:	bool
#
#
# LineUp(self)
#
# Same as ScrollLines (-1).
# Return type:	bool
#
#
# Lower(self)
#
# Lowers the window to the bottom of the window hierarchy (Z-order).
#
# Note
#
# This function only works for TopLevelWindow-derived classes.
#
# See also
#
# Raise
#
#
# MacIsWindowScrollbar(self, sb)
#
# Is the given widget one of this window’s built-in scrollbars? Only applicable on Mac.
#
#
# Move(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# Move (self, x, y, flags=SIZE_USE_EXISTING)
#
# Moves the window to the given position.
# Parameters:
#
# x (int) – Required x position.
# y (int) – Required y position.
# flags (int) – See SetSize for more info about this parameter.
#
# Note
#
# Implementations of SetSize can also implicitly implement the Move function, which is defined in the base wx.Window class as the call:
#
# self.SetSize(x, y, -1, -1, wx.SIZE_USE_EXISTING)
#
# See also
#
# SetSize
#
#
# Move (self, pt, flags=SIZE_USE_EXISTING)
#
# Moves the window to the given position.
# Parameters:
#
# pt (wx.Point) – wx.Point object representing the position.
# flags (int) – See SetSize for more info about this parameter.
#
# Note
#
# Implementations of SetSize can also implicitly implement the Move function, which is defined in the base wx.Window class as the call:
#
# self.SetSize(x, y, -1, -1, wx.SIZE_USE_EXISTING)
#
# See also
#
# SetSize
#
#
#
# MoveAfterInTabOrder(self, win)
#
# Moves this window in the tab navigation order after the specified win.
#
# This means that when the user presses TAB key on that other window, the focus switches to this window.
#
# Default tab order is the same as creation order, this function and MoveBeforeInTabOrder allow to change it after creating all the windows.
# Parameters:	win (wx.Window) – A sibling of this window which should precede it in tab order, must not be None
#
#
# MoveBeforeInTabOrder(self, win)
#
# Same as MoveAfterInTabOrder except that it inserts this window just before win instead of putting it right after it.
# Parameters:	win (wx.Window) –
#
#
# Navigate(self, flags=NavigationKeyEvent.IsForward)
#
# Performs a keyboard navigation action starting from this window.
#
# This method is equivalent to calling NavigateIn method on the parent window.
# Parameters:	flags (int) – A combination of wx.NavigationKeyEvent.IsForward and wx.NavigationKeyEvent.WinChange .
# Return type:	bool
# Returns:	Returns True if the focus was moved to another window or False if nothing changed.
#
# Note
#
# You may wish to call this from a text control custom keypress handler to do the default navigation behaviour for the tab key, since the standard default behaviour for a multiline text control with the wx.TE_PROCESS_TAB style is to insert a tab and not navigate to the next control. See also wx.NavigationKeyEvent and HandleAsNavigationKey.
#
#
# NavigateIn(self, flags=NavigationKeyEvent.IsForward)
#
# Performs a keyboard navigation action inside this window.
#
# See Navigate for more information.
#     Parameters:	flags (int) –
# Return type:	bool
#
#
# static NewControlId(count=1)
#
# Create a new ID or range of IDs that are not currently in use.
#
# The IDs will be reserved until assigned to a wx.Window ID or unreserved with UnreserveControlId .
#
# See Window IDs for more information.
#     Parameters:	count (int) – The number of sequential IDs to reserve.
# Return type:	wx.WindowID
# Returns:	Returns the ID or the first ID of the range (i.e. the most negative), or wx.ID_NONE if the specified number of identifiers couldn’t be allocated.
#
# See also
#
# UnreserveControlId , wx.IdManager, Window IDs
#
#
# OnInternalIdle(self)
#
# This virtual function is normally only used internally, but sometimes an application may need it to implement functionality that should not be disabled by an application defining an OnIdle handler in a derived class.
#
# This function may be used to do delayed painting, for example, and most implementations call UpdateWindowUI in order to send update events to the window in idle time.
#
#
# PageDown(self)
#
# Same as ScrollPages (1).
# Return type:	bool
#
#
# PageUp(self)
#
# Same as ScrollPages (-1).
# Return type:	bool
#
#
# PopEventHandler(self, deleteHandler=False)
#
# Removes and returns the top-most event handler on the event handler stack.
#
# E.g. in the case of:
# _images/overview_events_winstack1.png
#
# when calling W-> PopEventHandler , the event handler A will be removed and B will be the first handler of the stack.
#
# Note that it’s an error to call this function when no event handlers were pushed on this window (i.e. when the window itself is its only event handler).
# Parameters:	deleteHandler (bool) – If this is True, the handler will be deleted after it is removed (and the returned value will be None).
# Return type:	wx.EvtHandler
#
# See also
#
# How Events are Processed
#
#
# PopupMenu(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# PopupMenu (self, menu, pos=DefaultPosition)
#
# Pops up the given menu at the specified coordinates, relative to this window, and returns control when the user has dismissed the menu.
#
# If a menu item is selected, the corresponding menu event is generated and will be processed as usual. If coordinates are not specified, the current mouse cursor position is used.
#
# menu is the menu to pop up.
#
# The position where the menu will appear can be specified either as a wx.Point pos or by two integers (x and y).
# Parameters:
#
# menu (wx.Menu) –
# pos (wx.Point) –
#
# Return type:
#
# bool
#
# Note
#
# Just before the menu is popped up, wx.Menu.UpdateUI is called to ensure that the menu items are in the correct state. The menu does not get deleted by the window. It is recommended to not explicitly specify coordinates when calling PopupMenu in response to mouse click, because some of the ports (namely, wxGTK) can do a better job of positioning the menu in that case.
#
# See also
#
# wx.Menu
#
#
# PopupMenu (self, menu, x, y)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:
#
# menu (wx.Menu) –
# x (int) –
# y (int) –
#
# Return type:
#
# bool
#
#
#
# PostSizeEvent(self)
#
# Posts a size event to the window.
#
# This is the same as SendSizeEvent with SEND_EVENT_POST argument.
#
#
# PostSizeEventToParent(self)
#
# Posts a size event to the parent of this window.
#
# This is the same as SendSizeEventToParent with SEND_EVENT_POST argument.
#
#
# ProcessEvent(self, event)
#
# This function is public in wx.EvtHandler but protected in wx.Window because for Windows you should always call wx.ProcessEvent on the pointer returned by GetEventHandler and not on the wx.Window object itself.
#
# For convenience, a ProcessWindowEvent method is provided as a synonym for:
#
# self.GetEventHandler().ProcessEvent()
#
# Note that it’s still possible to call these functions directly on the wx.Window object (e.g. casting it to wx.EvtHandler) but doing that will create subtle bugs when windows with event handlers pushed on them are involved.
#
# This holds also for all other wx.EvtHandler functions.
# Parameters:	event (wx.Event) –
# Return type:	bool
#
#
# ProcessWindowEvent(self, event)
#
# Convenient wrapper for wx.ProcessEvent.
#
# This is the same as writing:
#
# self.GetEventHandler().ProcessEvent(event)
#
# but more convenient. Notice that wx.ProcessEvent itself can’t be called for wx.Window objects as it ignores the event handlers associated with the window; use this function instead.
# Parameters:	event (wx.Event) –
# Return type:	bool
#
#
# ProcessWindowEventLocally(self, event)
#
# Wrapper for wx.EvtHandler.ProcessEventLocally .
#
# This method is similar to ProcessWindowEvent but can be used to search for the event handler only in this window and any event handlers pushed on top of it. Unlike ProcessWindowEvent it won’t propagate the event upwards. But it will use the validator and event handlers associated with this window, if any.
# Parameters:	event (wx.Event) –
# Return type:	bool
#
# New in version 2.9.1.
#
#
# PushEventHandler(self, handler)
#
# Pushes this event handler onto the event stack for the window.
#
# An event handler is an object that is capable of processing the events sent to a window. By default, the window is its own event handler, but an application may wish to substitute another, for example to allow central implementation of event-handling for a variety of different window classes.
#
# wx.Window.PushEventHandler allows an application to set up a stack of event handlers, where an event not handled by one event handler is handed to the next one in the chain.
#
# E.g. if you have two event handlers A and B and a wx.Window instance W and you call:
#
# W.PushEventHandler(A)
# W.PushEventHandler(B)
#
# you will end up with the following situation:
#     _images/overview_events_winstack1.png
#
# Note that you can use wx.Window.PopEventHandler to remove the event handler.
# Parameters:	handler (wx.EvtHandler) – Specifies the handler to be pushed. It must not be part of a wx.EvtHandler chain; an assert will fail if it’s not unlinked (see wx.EvtHandler.IsUnlinked ).
#
# See also
#
# How Events are Processed
#
#
# Raise(self)
#
# Raises the window to the top of the window hierarchy (Z-order).
#
# Notice that this function only requests the window manager to raise this window to the top of Z-order. Depending on its configuration, the window manager may raise the window, not do it at all or indicate that a window requested to be raised in some other way, e.g. by flashing its icon if it is minimized.
#
# Note
#
# This function only works for TopLevelWindow-derived classes.
#
# See also
#
# Lower
#
#
# Refresh(self, eraseBackground=True, rect=None)
#
# Causes this window, and all of its children recursively (except under GTK1 where this is not implemented), to be repainted.
#
#     Note that repainting doesn’t happen immediately but only during the next event loop iteration, if you need to update the window immediately you should use Update instead.
# Parameters:
#
#     eraseBackground (bool) – If True, the background will be erased.
#     rect (wx.Rect) – If not None, only the given rectangle will be treated as damaged.
#
#     See also
#
# RefreshRect
#
#
# RefreshRect(self, rect, eraseBackground=True)
#
# Redraws the contents of the given rectangle: only the area inside it will be repainted.
#
#                                                                                  This is the same as Refresh but has a nicer syntax as it can be called with a temporary wx.Rect object as argument like this RefreshRect(wxRect(x, y, w, h)) .
# Parameters:
#
#     rect (wx.Rect) –
# eraseBackground (bool) –
#
#
# RegisterHotKey(self, hotkeyId, modifiers, virtualKeyCode)
#
# Registers a system wide hotkey.
#
#     Every time the user presses the hotkey registered here, this window will receive a hotkey event.
#
#     It will receive the event even if the application is in the background and does not have the input focus because the user is working with some other application.
# Parameters:
#
#     hotkeyId (int) – Numeric identifier of the hotkey. For applications this must be between 0 and 0xBFFF. If this function is called from a shared DLL, it must be a system wide unique identifier between 0xC000 and 0xFFFF. This is a MSW specific detail.
#     modifiers (int) – A bitwise combination of wx.MOD_SHIFT, wx.MOD_CONTROL, wx.MOD_ALT or wx.MOD_WIN specifying the modifier keys that have to be pressed along with the key.
# virtualKeyCode (int) – The virtual key code of the hotkey.
#
# Return type:
#
#     bool
# Returns:
#
# True if the hotkey was registered successfully. False if some other application already registered a hotkey with this modifier/virtualKeyCode combination.
#
# Note
#
# Use EVT_HOTKEY(hotkeyId, fnc) in the event table to capture the event. This function is currently only implemented under Windows. It is used in the Windows CE port for detecting hardware button presses.
#
# See also
#
# UnregisterHotKey
#
#
# ReleaseMouse(self)
#
# Releases mouse input captured with CaptureMouse .
#
# See also
#
# CaptureMouse , HasCapture , ReleaseMouse , wx.MouseCaptureLostEvent, wx.MouseCaptureChangedEvent
#
#
# RemoveChild(self, child)
#
# Removes a child window.
#
# This is called automatically by window deletion functions so should not be required by the application programmer. Notice that this function is mostly internal to wxWidgets and shouldn’t be called by the user code.
# Parameters:	child (wx.WindowBase) – Child window to remove.
#
#
#     RemoveEventHandler(self, handler)
#
# Find the given handler in the windows event handler stack and removes (but does not delete) it from the stack.
#
# See wx.EvtHandler.Unlink for more info.
#     Parameters:	handler (wx.EvtHandler) – The event handler to remove, must be not None and must be present in this windows event handlers stack.
#     Return type:	bool
# Returns:	Returns True if it was found and False otherwise (this also results in an assert failure so this function should only be called when the handler is supposed to be there).
#
# See also
#
# PushEventHandler , PopEventHandler
#
#
# Reparent(self, newParent)
#
# Reparents the window, i.e. the window will be removed from its current parent window (e.g.
#
# a non-standard toolbar in a wx.Frame) and then re-inserted into another.
#
#     Notice that currently you need to explicitly call wx.Notebook.RemovePage before reparenting a notebook page.
# Parameters:	newParent (wx.Window) – New parent.
#     Return type:	bool
#
#
# ScreenToClient(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# ScreenToClient (self, x, y)
#
# Converts from screen to client window coordinates.
# Parameters:
#
# x (int) – Stores the screen x coordinate and receives the client x coordinate.
#     y (int) – Stores the screen x coordinate and receives the client x coordinate.
#
#     Return type:
#
# tuple
# Returns:
#
# ( x, y )
#
#
# ScreenToClient (self, pt)
#
# Converts from screen to client window coordinates.
# Parameters:	pt (wx.Point) – The screen position.
#     Return type:	wx.Point
#
#
#
# ScrollLines(self, lines)
#
# Scrolls the window by the given number of lines down (if lines is positive) or up.
# Parameters:	lines (int) –
# Return type:	bool
# Returns:	Returns True if the window was scrolled, False if it was already on top/bottom and nothing was done.
#
#     Note
#
# This function is currently only implemented under MSW and wx.TextCtrl under wxGTK (it also works for wx.Scrolled classes under all platforms).
#
# See also
#
# ScrollPages
#
#
# ScrollPages(self, pages)
#
# Scrolls the window by the given number of pages down (if pages is positive) or up.
# Parameters:	pages (int) –
# Return type:	bool
# Returns:	Returns True if the window was scrolled, False if it was already on top/bottom and nothing was done.
#
#     Note
#
# This function is currently only implemented under MSW and wxGTK.
#
#     See also
#
# ScrollLines
#
#
# ScrollWindow(self, dx, dy, rect=None)
#
# Physically scrolls the pixels in the window and move child windows accordingly.
# Parameters:
#
# dx (int) – Amount to scroll horizontally.
#     dy (int) – Amount to scroll vertically.
#     rect (wx.Rect) – Rectangle to scroll, if it is None, the whole window is scrolled (this is always the case under wxGTK which doesn’t support this parameter)
#
# Note
#
# Note that you can often use wx.Scrolled instead of using this function directly.
#
#
# SendDestroyEvent(self)
#
# Generate wx.WindowDestroyEvent for this window.
#
# This is called by the window itself when it is being destroyed and usually there is no need to call it but see wx.WindowDestroyEvent for explanations of when you might want to do it.
#
#
# SendIdleEvents(self, event)
#
# Send idle event to window and all subwindows.
#
# Returns True if more idle time is requested.
# Parameters:	event (wx.IdleEvent) –
# Return type:	bool
#
#
# SendSizeEvent(self, flags=0)
#
# This function sends a dummy size event to the window allowing it to re-layout its children positions.
#
#                                                                                                It is sometimes useful to call this function after adding or deleting a children after the frame creation or if a child size changes. Note that if the frame is using either sizers or constraints for the children layout, it is enough to call wx.Window.Layout directly and this function should not be used in this case.
#
# If flags includes SEND_EVENT_POST value, this function posts the event, i.e. schedules it for later processing, instead of dispatching it directly. You can also use PostSizeEvent as a more readable equivalent of calling this function with this flag.
# Parameters:	flags (int) – May include SEND_EVENT_POST . Default value is 0.
#
#
# SendSizeEventToParent(self, flags=0)
#
# Safe wrapper for GetParent . SendSizeEvent .
#
# This function simply checks that the window has a valid parent which is not in process of being deleted and calls SendSizeEvent on it. It is used internally by windows such as toolbars changes to whose state should result in parent re-layout (e.g. when a toolbar is added to the top of the window, all the other windows must be shifted down).
# Parameters:	flags (int) – See description of this parameter in SendSizeEvent documentation.
#
#     See also
#
# PostSizeEventToParent
#
#
# SetAcceleratorTable(self, accel)
#
# Sets the accelerator table for this window.
#
#     See wx.AcceleratorTable.
# Parameters:	accel (wx.AcceleratorTable) –
#
#
# SetAccessible(self, accessible)
#
# Sets the accessible for this window.
#
#     Any existing accessible for this window will be deleted first, if not identical to accessible. See also wx.Accessible.
# Parameters:	accessible (wx.Accessible) –
#
#
# SetAutoLayout(self, autoLayout)
#
# Determines whether the Layout function will be called automatically when the window is resized.
#
#     This method is called implicitly by SetSizer but if you use SetConstraints you should call it manually or otherwise the window layout won’t be correctly updated when its size changes.
# Parameters:	autoLayout (bool) – Set this to True if you wish the Layout function to be called automatically when the window is resized.
#
#     See also
#
# SetSizer , SetConstraints
#
#
# SetBackgroundColour(self, colour)
#
# Sets the background colour of the window.
#
#     Notice that as with SetForegroundColour , setting the background colour of a native control may not affect the entire control and could be not supported at all depending on the control and platform.
#
# Please see InheritAttributes for explanation of the difference between this method and SetOwnBackgroundColour .
# Parameters:	colour (wx.Colour) – The colour to be used as the background colour; pass NullColour to reset to the default colour. Note that you may want to use wx.SystemSettings.GetColour to retrieve a suitable colour to use rather than setting an hard-coded one.
#     Return type:	bool
# Returns:	True if the colour was really changed, False if it was already set to this colour and nothing was done.
#
#     Note
#
# The background colour is usually painted by the default wx.EraseEvent event handler function under Windows and automatically under GTK. Note that setting the background colour does not cause an immediate refresh, so you may wish to call wx.Window.ClearBackground or wx.Window.Refresh after calling this function. Using this function will disable attempts to use themes for this window, if the system supports them. Use with care since usually the themes represent the appearance chosen by the user to be used for all applications on the system.
#
# See also
#
# GetBackgroundColour , SetForegroundColour , GetForegroundColour , ClearBackground , Refresh , wx.EraseEvent, wx.SystemSettings
#
#
# SetBackgroundStyle(self, style)
#
# Sets the background style of the window.
#
# The default background style is BG_STYLE_ERASE which indicates that the window background may be erased in EVT_ERASE_BACKGROUND handler. This is a safe, compatibility default; however you may want to change it to BG_STYLE_SYSTEM if you don’t define any erase background event handlers at all, to avoid unnecessary generation of erase background events and always let system erase the background. And you should change the background style to BG_STYLE_PAINT if you define an EVT_PAINT handler which completely overwrites the window background as in this case erasing it previously, either in EVT_ERASE_BACKGROUND handler or in the system default handler, would result in flicker as the background pixels will be repainted twice every time the window is redrawn. Do ensure that the background is entirely erased by your EVT_PAINT handler in this case however as otherwise garbage may be left on screen.
#
# Notice that in previous versions of wxWidgets a common way to work around the above mentioned flickering problem was to define an empty EVT_ERASE_BACKGROUND handler. Setting background style to BG_STYLE_PAINT is a simpler and more efficient solution to the same problem.
#
# Under wxGTK and wxOSX, you can use BG_STYLE_TRANSPARENT to obtain full transparency of the window background. Note that wxGTK supports this only since GTK 2.12 with a compositing manager enabled, call IsTransparentBackgroundSupported to check whether this is the case.
#
# Also, on order for SetBackgroundStyle(wxBG_STYLE_TRANSPARENT) to work, it must be called before Create . If you’re using your own Window-derived class you should write your code in the following way:
#
# class MyWidget(wx.Window):
#
#     def __init__(self, parent):
#
#         wx.Window.__init__(self) # Use default constructor here!
#
#         # Do this first:
#         self.SetBackgroundStyle(wx.BG_STYLE_TRANSPARENT)
#
#         # And really create the window afterwards:
#         self.Create(parent)
#
# Parameters:	style (BackgroundStyle) –
# Return type:	bool
#
# See also
#
# SetBackgroundColour , GetForegroundColour , SetTransparent , IsTransparentBackgroundSupported
#
#
# SetCanFocus(self, canFocus)
#
# This method is only implemented by ports which have support for native TAB traversal (such as GTK+ 2.0).
#
# It is called by wxWidgets’ container control code to give the native system a hint when doing TAB traversal. A call to this does not disable or change the effect of programmatically calling SetFocus .
# Parameters:	canFocus (bool) –
#
# See also
#
# wx.FocusEvent, wx.Panel.SetFocus , wx.Panel.SetFocusIgnoringChildren
#
#
# SetCaret(self, caret)
#
# Sets the caret() associated with the window.
# Parameters:	caret (wx.Caret) –
#
#
# SetClientRect(self, rect)
#
#
# SetClientSize(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# SetClientSize (self, width, height)
#
# This sets the size of the window client area in pixels.
#
# Using this function to size a window tends to be more device-independent than SetSize , since the application need not worry about what dimensions the border or title bar have when trying to fit the window around panel items, for example.
#     Parameters:
#
# width (int) –
# height (int) –
#
# See also
#
# Window Sizing Overview
#
#
# SetClientSize (self, size)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	size (wx.Size) –
#
#
# SetClientSize (self, rect)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	rect (wx.Rect) –
#
#
#
# SetConstraints(self, constraints)
#
# Sets the window to have the given layout constraints.
#
# The window will then own the object, and will take care of its deletion. If an existing layout constraints object is already owned by the window, it will be deleted.
# Parameters:	constraints (wx.LayoutConstraints) – The constraints to set. Pass None to disassociate and delete the window’s constraints.
#
# Note
#
# You must call SetAutoLayout to tell a window to use the constraints automatically in OnSize; otherwise, you must override OnSize and call Layout explicitly. When setting both a wx.LayoutConstraints and a wx.Sizer, only the sizer will have effect.
#
#
# SetContainingSizer(self, sizer)
#
# This normally does not need to be called by user code.
#
# It is called when a window is added to a sizer, and is used so the window can remove itself from the sizer when it is destroyed.
# Parameters:	sizer (wx.Sizer) –
#
#
# SetCursor(self, cursor)
#
# Sets the window’s cursor.
#
# Notice that the window cursor also sets it for the children of the window implicitly.
#
# The cursor may be NullCursor in which case the window cursor will be reset back to default.
# Parameters:	cursor (wx.Cursor) – Specifies the cursor that the window should normally display.
# Return type:	bool
#
# See also
#
# wx.SetCursor , wx.Cursor
#
#
# SetDimensions(self, x, y, width, height, sizeFlags=SIZE_AUTO)
#
#
# SetDoubleBuffered(self, on)
#
# Turn on or off double buffering of the window if the system supports it.
# Parameters:	on (bool) –
#
#
# SetDropTarget(self, target)
#
# Associates a drop target with this window.
#
# If the window already has a drop target, it is deleted.
# Parameters:	target (wx.DropTarget) –
#
# See also
#
# GetDropTarget , Drag and Drop Overview
#
#
# SetEventHandler(self, handler)
#
# Sets the event handler for this window.
#
# Note that if you use this function you may want to use as the “next” handler of handler the window itself; in this way when handler doesn’t process an event, the window itself will have a chance to do it.
# Parameters:	handler (wx.EvtHandler) – Specifies the handler to be set. Cannot be None.
#
# See also
#
# How Events are Processed
#
#
# SetExtraStyle(self, exStyle)
#
# Sets the extra style bits for the window.
#
# The currently defined extra style bits are reported in the class description.
# Parameters:	exStyle (long) –
#
#
# SetFocus(self)
#
# This sets the window to receive keyboard input.
#
# See also
#
# HasFocus , wx.FocusEvent, wx.Panel.SetFocus , wx.Panel.SetFocusIgnoringChildren
#
#
# SetFocusFromKbd(self)
#
# This function is called by wxWidgets keyboard navigation code when the user gives the focus to this window from keyboard (e.g.
#
#     using TAB key).
#
# By default this method simply calls SetFocus but can be overridden to do something in addition to this in the derived classes.
#
#
# SetFont(self, font)
#
# Sets the font for this window.
#
# This function should not be called for the parent window if you don’t want its font to be inherited by its children, use SetOwnFont instead in this case and see InheritAttributes for more explanations.
#
# Please notice that the given font is not automatically used for wx.PaintDC objects associated with this window, you need to call wx.DC.SetFont too. However this font is used by any standard controls for drawing their text as well as by GetTextExtent .
# Parameters:	font (wx.Font) – Font to associate with this window, pass NullFont to reset to the default font.
# Return type:	bool
# Returns:	True if the font was really changed, False if it was already set to this font and nothing was done.
#
# See also
#
# GetFont , InheritAttributes
#
#
# SetForegroundColour(self, colour)
#
# Sets the foreground colour of the window.
#
# The meaning of foreground colour varies according to the window class; it may be the text colour or other colour, or it may not be used at all. Additionally, not all native controls support changing their foreground colour so this method may change their colour only partially or even not at all.
#
# Please see InheritAttributes for explanation of the difference between this method and SetOwnForegroundColour .
# Parameters:	colour (wx.Colour) – The colour to be used as the foreground colour; pass NullColour to reset to the default colour.
# Return type:	bool
# Returns:	True if the colour was really changed, False if it was already set to this colour and nothing was done.
#
# See also
#
# GetForegroundColour , SetBackgroundColour , GetBackgroundColour , ShouldInheritColours
#
#
# SetHelpText(self, helpText)
#
# Sets the help text to be used as context-sensitive help for this window.
#
# Note that the text is actually stored by the current wx.HelpProvider implementation, and not in the window object itself.
# Parameters:	helpText (string) –
#
# See also
#
# GetHelpText , wx.HelpProvider.AddHelp
#
#
# SetId(self, winid)
#
# Sets the identifier of the window.
# Parameters:	winid (wx.WindowID) –
#
# Note
#
# Each window has an integer identifier. If the application has not provided one, an identifier will be generated. Normally, the identifier should be provided on creation and should not be modified subsequently.
#
# See also
#
# GetId , Window IDs
#
#
# SetInitialSize(self, size=DefaultSize)
#
# A smart SetSize that will fill in default size components with the window’s best size values.
#
# Also sets the window’s minsize to the value passed in for use with sizers. This means that if a full or partial size is passed to this function then the sizers will use that size instead of the results of GetBestSize to determine the minimum needs of the window for layout.
#
# Most controls will use this to set their initial size, and their min size to the passed in value (if any.)
# Parameters:	size (wx.Size) –
#
# See also
#
# SetSize , GetBestSize , GetEffectiveMinSize , Window Sizing Overview
#
#
# SetLabel(self, label)
#
# Sets the window’s label.
# Parameters:	label (string) – The window label.
#
# See also
#
# GetLabel
#
#
# SetLayoutDirection(self, dir)
#
# Sets the layout direction for this window.
#
# This function is only supported under MSW and GTK platforms, but not under Mac currently.
# Parameters:	dir (LayoutDirection) –
#
#
# SetMaxClientSize(self, size)
#
# Sets the maximum client size of the window, to indicate to the sizer layout mechanism that this is the maximum possible size of its client area.
#
# Note that this method is just a shortcut for:
#
# self.SetMaxSize(self.ClientToWindowSize(size))
#
# Parameters:	size (wx.Size) –
#
# See also
#
# SetMaxSize , Window Sizing Overview
#
#
# SetMaxSize(self, size)
#
# Sets the maximum size of the window, to indicate to the sizer layout mechanism that this is the maximum possible size.
# Parameters:	size (wx.Size) –
#
# See also
#
# SetMaxClientSize , Window Sizing Overview
#
#
# SetMinClientSize(self, size)
#
# Sets the minimum client size of the window, to indicate to the sizer layout mechanism that this is the minimum required size of window’s client area.
#
# You may need to call this if you change the window size after construction and before adding to its parent sizer.
#
# Note, that just as with SetMinSize , calling this method doesn’t prevent the program from explicitly making the window smaller than the specified size.
#
# Note that this method is just a shortcut for:
#
# self.SetMinSize(self.ClientToWindowSize(size))
#
# Parameters:	size (wx.Size) –
#
# See also
#
# SetMinSize , Window Sizing Overview
#
#
# SetMinSize(self, size)
#
# Sets the minimum size of the window, to indicate to the sizer layout mechanism that this is the minimum required size.
#
# You may need to call this if you change the window size after construction and before adding to its parent sizer.
#
# Notice that calling this method doesn’t prevent the program from making the window explicitly smaller than the specified size by calling SetSize , it just ensures that it won’t become smaller than this size during the automatic layout.
# Parameters:	size (wx.Size) –
#
# See also
#
# SetMinClientSize , Window Sizing Overview
#
#
# SetName(self, name)
#
# Sets the window’s name.
# Parameters:	name (string) – A name to set for the window.
#
# See also
#
# GetName
#
#
# SetNextHandler(self, handler)
#
# Windows cannot be used to form event handler chains; this function thus will assert when called.
#
# Note that instead you can use PushEventHandler or SetEventHandler to implement a stack of event handlers to override wx.Window‘s own event handling mechanism.
# Parameters:	handler (wx.EvtHandler) –
#
#
# SetOwnBackgroundColour(self, colour)
#
# Sets the background colour of the window but prevents it from being inherited by the children of this window.
# Parameters:	colour (wx.Colour) –
#
# See also
#
# SetBackgroundColour , InheritAttributes
#
#
# SetOwnFont(self, font)
#
# Sets the font of the window but prevents it from being inherited by the children of this window.
# Parameters:	font (wx.Font) –
#
# See also
#
# SetFont , InheritAttributes
#
#
# SetOwnForegroundColour(self, colour)
#
# Sets the foreground colour of the window but prevents it from being inherited by the children of this window.
# Parameters:	colour (wx.Colour) –
#
# See also
#
# SetForegroundColour , InheritAttributes
#
#
# SetPalette(self, pal)
# Parameters:	pal (wx.Palette) –
#
# Deprecated
#
# use wx.DC.SetPalette instead.
#
#
# SetPosition(self, pt)
#
# Moves the window to the specified position.
#
# This is exactly the same as calling Move with the default arguments.
# Parameters:	pt (wx.Point) –
#
#
# SetPreviousHandler(self, handler)
#
# Windows cannot be used to form event handler chains; this function thus will assert when called.
#
# Note that instead you can use PushEventHandler or SetEventHandler to implement a stack of event handlers to override wx.Window‘s own event handling mechanism.
# Parameters:	handler (wx.EvtHandler) –
#
#
# SetRect(self, rect)
#
#
# SetScrollPos(self, orientation, pos, refresh=True)
#
# Sets the position of one of the built-in scrollbars.
# Parameters:
#
# orientation (int) – Determines the scrollbar whose position is to be set. May be wx.HORIZONTAL or wx.VERTICAL.
# pos (int) – Position in scroll units.
# refresh (bool) – True to redraw the scrollbar, False otherwise.
#
# Note
#
# This function does not directly affect the contents of the window: it is up to the application to take note of scrollbar attributes and redraw contents accordingly.
#
# See also
#
# SetScrollbar , GetScrollPos , GetScrollThumb , wx.ScrollBar, wx.Scrolled
#
#
# SetScrollbar(self, orientation, position, thumbSize, range, refresh=True)
#
# Sets the scrollbar properties of a built-in scrollbar.
# Parameters:
#
# orientation (int) – Determines the scrollbar whose page size is to be set. May be wx.HORIZONTAL or wx.VERTICAL.
# position (int) – The position of the scrollbar in scroll units.
# thumbSize (int) – The size of the thumb, or visible portion of the scrollbar, in scroll units.
# range (int) – The maximum position of the scrollbar. Value of -1 can be used to ask for the scrollbar to be shown but in the disabled state: this can be used to avoid removing the scrollbar even when it is not needed (currently this is only implemented in wxMSW port).
# refresh (bool) – True to redraw the scrollbar, False otherwise.
#
# Note
#
# Let’s say you wish to display 50 lines of text, using the same font. The window is sized so that you can only see 16 lines at a time. You would use:
#
# self.SetScrollbar(wx.VERTICAL, 0, 16, 50)
#
# Note that with the window at this size, the thumb position can never go above 50 minus 16, or 34. You can determine how many lines are currently visible by dividing the current view size by the character height in pixels. When defining your own scrollbar behaviour, you will always need to recalculate the scrollbar settings when the window size changes. You could therefore put your scrollbar calculations and SetScrollbar call into a function named AdjustScrollbars, which can be called initially and also from your wx.SizeEvent handler function.
#
# See also
#
# Scrolled Windows, wx.ScrollBar, wx.Scrolled, wx.ScrollWinEvent
#
#
# SetSize(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# SetSize (self, x, y, width, height, sizeFlags=SIZE_AUTO)
#
# Sets the size of the window in pixels.
# Parameters:
#
# x (int) – Required x position in pixels, or DefaultCoord to indicate that the existing value should be used.
# y (int) – Required y position in pixels, or DefaultCoord to indicate that the existing value should be used.
# width (int) – Required width in pixels, or DefaultCoord to indicate that the existing value should be used.
# height (int) – Required height position in pixels, or DefaultCoord to indicate that the existing value should be used.
# sizeFlags (int) – Indicates the interpretation of other parameters. It is a bit list of the following:
#
# SIZE_AUTO_WIDTH: a DefaultCoord width value is taken to indicate a Widgets-supplied default width.
# SIZE_AUTO_HEIGHT: a DefaultCoord height value is taken to indicate a Widgets-supplied default height.
# SIZE_AUTO: DefaultCoord size values are taken to indicate a Widgets-supplied default size.
# SIZE_USE_EXISTING: existing dimensions should be used if DefaultCoord values are supplied.
# SIZE_ALLOW_MINUS_ONE: allow negative dimensions (i.e. value of DefaultCoord) to be interpreted as real dimensions, not default values.
# SIZE_FORCE: normally, if the position and the size of the window are already the same as the parameters of this function, nothing is done. but with this flag a window resize may be forced even in this case (supported in 2.6.2 and later and only implemented for MSW and ignored elsewhere currently).
#
# Note
#
# This overload sets the position and optionally size, of the window. Parameters may be DefaultCoord to indicate either that a default should be supplied by wxWidgets, or that the current value of the dimension should be used.
#
# See also
#
# Move , Window Sizing Overview
#
#
# SetSize (self, rect)
#
# Sets the size of the window in pixels.
#
# The size is specified using a wx.Rect, wx.Size or by a couple of int objects.
# Parameters:	rect (wx.Rect) –
#
# Note
#
# This form must be used with non-default width and height values.
#
# See also
#
# Move , Window Sizing Overview
#
#
# SetSize (self, size)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	size (wx.Size) –
#
#
# SetSize (self, width, height)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:
#
# width (int) –
# height (int) –
#
#
#
# SetSizeHints(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# SetSizeHints (self, minSize, maxSize=DefaultSize, incSize=DefaultSize)
#
# Use of this function for windows which are not toplevel windows (such as wx.Dialog or wx.Frame) is discouraged.
#
# Please use SetMinSize and SetMaxSize instead.
# Parameters:
#
# minSize (wx.Size) –
# maxSize (wx.Size) –
# incSize (wx.Size) –
#
# See also
#
# wx.TopLevelWindow.SetSizeHints , Window Sizing Overview
#
#
# SetSizeHints (self, minW, minH, maxW=-1, maxH=-1, incW=-1, incH=-1)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:
#
# minW (int) –
# minH (int) –
# maxW (int) –
# maxH (int) –
# incW (int) –
# incH (int) –
#
#
#
# SetSizer(self, sizer, deleteOld=True)
#
# Sets the window to have the given layout sizer.
#
# The window will then own the object, and will take care of its deletion. If an existing layout constraints object is already owned by the window, it will be deleted if the deleteOld parameter is True.
#
# Note that this function will also call SetAutoLayout implicitly with True parameter if the sizer is not None and False otherwise so that the sizer will be effectively used to layout the window children whenever it is resized.
# Parameters:
#
# sizer (wx.Sizer) – The sizer to set. Pass None to disassociate and conditionally delete the window’s sizer. See below.
# deleteOld (bool) – If True (the default), this will delete any pre-existing sizer. Pass False if you wish to handle deleting the old sizer yourself but remember to do it yourself in this case to avoid memory leaks.
#
# Note
#
# SetSizer enables and disables Layout automatically.
#
#
# SetSizerAndFit(self, sizer, deleteOld=True)
#
# This method calls SetSizer and then wx.Sizer.SetSizeHints which sets the initial window size to the size needed to accommodate all sizer elements and sets the size hints which, if this window is a top level one, prevent the user from resizing it to be less than this minimal size.
# Parameters:
#
# sizer (wx.Sizer) –
# deleteOld (bool) –
#
#
# SetThemeEnabled(self, enable)
#
# This function tells a window if it should use the system’s “theme” code to draw the windows’ background instead of its own background drawing code.
#
# This does not always have any effect since the underlying platform obviously needs to support the notion of themes in user defined windows. One such platform is GTK+ where windows can have (very colourful) backgrounds defined by a user’s selected theme.
#
# Dialogs, notebook pages and the status bar have this flag set to True by default so that the default look and feel is simulated best.
# Parameters:	enable (bool) –
#
#
# SetToolTip(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# SetToolTip (self, tipString)
#
# Attach a tooltip to the window.
#
# wx.ToolTip pointer can be None in the overload taking the pointer, meaning to unset any existing tooltips; however UnsetToolTip provides a more readable alternative to this operation.
#
# Notice that these methods are always available, even if wxWidgets was compiled with USE_TOOLTIPS set to 0, but don’t do anything in this case.
# Parameters:	tipString (string) –
#
# See also
#
# GetToolTip , wx.ToolTip
#
#
# SetToolTip (self, tip)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	tip (wx.ToolTip) –
#
#
#
# SetTransparent(self, alpha)
#
# Set the transparency of the window.
#
# If the system supports transparent windows, returns True, otherwise returns False and the window remains fully opaque. See also CanSetTransparent .
#
# The parameter alpha is in the range 0..255 where 0 corresponds to a fully transparent window and 255 to the fully opaque one. The constants IMAGE_ALPHA_TRANSPARENT and IMAGE_ALPHA_OPAQUE can be used.
# Parameters:	alpha (wx.Byte) –
# Return type:	bool
#
#
# SetValidator(self, validator)
#
# Deletes the current validator (if any) and sets the window validator, having called wx.Validator.Clone to create a new validator of this type.
# Parameters:	validator (wx.Validator) –
#
#
# SetVirtualSize(self, *args, **kw)
#
# overload Overloaded Implementations:
#
#
# SetVirtualSize (self, width, height)
#
# Sets the virtual size of the window in pixels.
# Parameters:
#
# width (int) –
# height (int) –
#
# See also
#
# Window Sizing Overview
#
#
# SetVirtualSize (self, size)
#
# This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.
# Parameters:	size (wx.Size) –
#
#
#
# SetWindowStyle(self, style)
#
# See SetWindowStyleFlag for more info.
#     Parameters:	style (long) –
#
#
# SetWindowStyleFlag(self, style)
#
# Sets the style of the window.
#
# Please note that some styles cannot be changed after the window creation and that Refresh might need to be called after changing the others for the change to take place immediately.
#
# See Window styles for more information about flags.
# Parameters:	style (long) –
#
# See also
#
# GetWindowStyleFlag
#
#
# SetWindowVariant(self, variant)
#
# Chooses a different variant of the window display to use.
#
# Window variants currently just differ in size, as can be seen from wx.WindowVariant documentation. Under all platforms but OS X, this function does nothing more than change the font used by the window. However under OS X it is implemented natively and selects the appropriate variant of the native widget, which has better appearance than just scaled down or up version of the normal variant, so it should be preferred to directly tweaking the font size.
#
# By default the controls naturally use the normal variant.
# Parameters:	variant (WindowVariant) –
#
#
# ShouldInheritColours(self)
#
# Return True from here to allow the colours of this window to be changed by InheritAttributes .
#
# Returning False forbids inheriting them from the parent window.
#
# The base class version returns False, but this method is overridden in wx.Control where it returns True.
# Return type:	bool
#
#
# Show(self, show=True)
#
# Shows or hides the window.
#
# You may need to call Raise for a top level window if you want to bring it to top, although this is not needed if Show is called immediately after the frame creation.
#
# Notice that the default state of newly created top level windows is hidden (to allow you to create their contents without flicker) unlike for all the other, not derived from wx.TopLevelWindow, windows that are by default created in the shown state.
# Parameters:	show (bool) – If True displays the window. Otherwise, hides it.
# Return type:	bool
# Returns:	True if the window has been shown or hidden or False if nothing was done because it already was in the requested state.
#
# See also
#
# IsShown , Hide , wx.RadioBox.Show , wx.ShowEvent.
#
#
# ShowWithEffect(self, effect, timeout=0)
#
# This function shows a window, like Show , but using a special visual effect if possible.
# Parameters:
#
# effect (ShowEffect) – The effect to use.
# timeout (int) – The timeout parameter specifies the time of the animation, in milliseconds. If the default value of 0 is used, the default animation time for the current platform is used.
#
# Return type:
#
# bool
#
# New in version 2.9.0.
#
# Note
#
# Currently this function is only implemented in wxMSW and wxOSX (for TopLevelWindows only in Carbon version and for any kind of windows in Cocoa) and does the same thing as Show in the other ports.
#
# See also
#
# HideWithEffect
#
#
# Thaw(self)
#
# Re-enables window updating after a previous call to Freeze .
#
# To really thaw the control, it must be called exactly the same number of times as Freeze .
#
# If the window has any children, they are recursively thawed too.
#
# See also
#
# WindowUpdateLocker , Freeze , IsFrozen
#
#
# ToggleWindowStyle(self, flag)
#
# Turns the given flag on if it’s currently turned off and vice versa.
#
# This function cannot be used if the value of the flag is 0 (which is often the case for default flags).
#
# Also, please notice that not all styles can be changed after the control creation.
# Parameters:	flag (int) –
# Return type:	bool
# Returns:	Returns True if the style was turned on by this function, False if it was switched off.
#
# See also
#
# SetWindowStyleFlag , HasFlag
#
#
# TransferDataFromWindow(self)
#
# Transfers values from child controls to data areas specified by their validators.
#
# Returns False if a transfer failed.
#
# If the window has WS_EX_VALIDATE_RECURSIVELY extra style flag set, the method will also call TransferDataFromWindow of all child windows.
# Return type:	bool
#
# See also
#
# TransferDataToWindow , wx.Validator, Validate
#
#
# TransferDataToWindow(self)
#
# Transfers values to child controls from data areas specified by their validators.
#
# If the window has WS_EX_VALIDATE_RECURSIVELY extra style flag set, the method will also call TransferDataToWindow of all child windows.
# Return type:	bool
# Returns:	Returns False if a transfer failed.
#
# See also
#
# TransferDataFromWindow , wx.Validator, Validate
#
#
# UnregisterHotKey(self, hotkeyId)
#
# Unregisters a system wide hotkey.
# Parameters:	hotkeyId (int) – Numeric identifier of the hotkey. Must be the same id that was passed to RegisterHotKey .
# Return type:	bool
# Returns:	True if the hotkey was unregistered successfully, False if the id was invalid.
#
# Note
#
# This function is currently only implemented under MSW.
#
# See also
#
# RegisterHotKey
#
#
# static UnreserveControlId(id, count=1)
#
# Unreserve an ID or range of IDs that was reserved by NewControlId .
#
# See Window IDs for more information.
#     Parameters:
#
# id (wx.WindowID) – The starting ID of the range of IDs to unreserve.
# count (int) – The number of sequential IDs to unreserve.
#
# See also
#
# NewControlId , wx.IdManager, Window IDs
#
#
# UnsetToolTip(self)
#
# Unset any existing tooltip.
#
# New in version 2.9.0.
#
# See also
#
# SetToolTip
#
#
# Update(self)
#
# Calling this method immediately repaints the invalidated area of the window and all of its children recursively (this normally only happens when the flow of control returns to the event loop).
#
# Notice that this function doesn’t invalidate any area of the window so nothing happens if nothing has been invalidated (i.e. marked as requiring a redraw). Use Refresh first if you want to immediately redraw the window unconditionally.
#
#
# UpdateWindowUI(self, flags=UPDATE_UI_NONE)
#
# This function sends one or more wx.UpdateUIEvent to the window.
#
# The particular implementation depends on the window; for example a wx.ToolBar will send an update UI event for each toolbar button, and a wx.Frame will send an update UI event for each menubar menu item.
#
# You can call this function from your application to ensure that your UI is up-to-date at this point (as far as your wx.UpdateUIEvent handlers are concerned). This may be necessary if you have called wx.UpdateUIEvent.SetMode or wx.UpdateUIEvent.SetUpdateInterval to limit the overhead that wxWidgets incurs by sending update UI events in idle time. flags should be a bitlist of one or more of the wx.UpdateUI enumeration.
#
# If you are calling this function from an OnInternalIdle or OnIdle function, make sure you pass the wx.UPDATE_UI_FROMIDLE flag, since this tells the window to only update the UI elements that need to be updated in idle time. Some windows update their elements only when necessary, for example when a menu is about to be shown. The following is an example of how to call UpdateWindowUI from an idle function.
#
# def OnInternalIdle(self):
#
#     if wx.UpdateUIEvent.CanUpdate(self):
#         self.UpdateWindowUI(wx.UPDATE_UI_FROMIDLE)
#
# Parameters:	flags (long) –
#
# See also
#
# wx.UpdateUIEvent, DoUpdateWindowUI , OnInternalIdle
#
#
# UseBgCol(self)
#
# Return True if a background colour has been set for this window.
#     Return type:	bool
#
#
# Validate(self)
#
# Validates the current values of the child controls using their validators.
#
# If the window has WS_EX_VALIDATE_RECURSIVELY extra style flag set, the method will also call Validate of all child windows.
# Return type:	bool
# Returns:	Returns False if any of the validations failed.
#
# See also
#
# TransferDataFromWindow , TransferDataToWindow , wx.Validator
#
#
# WarpPointer(self, x, y)
#
# Moves the pointer to the given position on the window.
# Parameters:
#
# x (int) – The new x position for the cursor.
#     y (int) – The new y position for the cursor.
#
# Note
#
# Apple Human Interface Guidelines forbid moving the mouse cursor programmatically so you should avoid using this function in Mac applications (and probably avoid using it under the other platforms without good reason as well).
#
#
# WindowToClientSize(self, size)
#
# Converts window size size to corresponding client area size In other words, the returned value is what would GetClientSize return if this window had given window size.
#
# Components with DefaultCoord value are left unchanged.
#
# Note that the conversion is not always exact, it assumes that non-client area doesn’t change and so doesn’t take into account things like menu bar (un)wrapping or (dis)appearance of the scrollbars.
# Parameters:	size (wx.Size) –
# Return type:	wx.Size
#
# New in version 2.8.8.
#
# See also
#
# ClientToWindowSize
#
#
# __nonzero__(self)
#
# Can be used to test if the C++ part of the window still exists, with code like this:
#
# if theWindow:
#     doSomething()
#
#
# Properties
#
# AcceleratorTable
#
# See GetAcceleratorTable and SetAcceleratorTable
#
#
# AutoLayout
#
# See GetAutoLayout and SetAutoLayout
#
#
# BackgroundColour
#
# See GetBackgroundColour and SetBackgroundColour
#
#
# BackgroundStyle
#
# See GetBackgroundStyle and SetBackgroundStyle
#
#
# BestSize
#
# See GetBestSize
#
#
# BestVirtualSize
#
# See GetBestVirtualSize
#
#
# Border
#
# See GetBorder
#
#
# Caret
#
# See GetCaret and SetCaret
#
#
# CharHeight
#
# See GetCharHeight
#
#
# CharWidth
#
# See GetCharWidth
#
#
# Children
#
# See GetChildren
#
#
# ClientAreaOrigin
#
# See GetClientAreaOrigin
#
#
# ClientRect
#
# See GetClientRect and SetClientRect
#
#
# ClientSize
#
# See GetClientSize and SetClientSize
#
#
# Constraints
#
# See GetConstraints and SetConstraints
#
#
# ContainingSizer
#
# See GetContainingSizer and SetContainingSizer
#
#
# Cursor
#
# See GetCursor and SetCursor
#
#
# DefaultAttributes
#
# See GetDefaultAttributes
#
#
# DropTarget
#
# See GetDropTarget and SetDropTarget
#
#
# EffectiveMinSize
#
# See GetEffectiveMinSize
#
#
# Enabled
#
# See IsEnabled and Enable
#
#
# EventHandler
#
# See GetEventHandler and SetEventHandler
#
#
# ExtraStyle
#
# See GetExtraStyle and SetExtraStyle
#
#
# Font
#
# See GetFont and SetFont
#
#
# ForegroundColour
#
# See GetForegroundColour and SetForegroundColour
#
#
# GrandParent
#
# See GetGrandParent
#
#
# Handle
#
# See GetHandle
#
#
# HelpText
#
# See GetHelpText and SetHelpText
#
#
# Id
#
# See GetId and SetId
#
#
# Label
#
# See GetLabel and SetLabel
#
#
# LayoutDirection
#
# See GetLayoutDirection and SetLayoutDirection
#
#
# MaxClientSize
#
# See GetMaxClientSize and SetMaxClientSize
#
#
# MaxHeight
#
# See GetMaxHeight
#
#
# MaxSize
#
# See GetMaxSize and SetMaxSize
#
#
# MaxWidth
#
# See GetMaxWidth
#
#
# MinClientSize
#
# See GetMinClientSize and SetMinClientSize
#
#
# MinHeight
#
# See GetMinHeight
#
#
# MinSize
#
# See GetMinSize and SetMinSize
#
#
# MinWidth
#
# See GetMinWidth
#
#
# Name
#
# See GetName and SetName
#
#
# Parent
#
# See GetParent
#
#
# Position
#
# See GetPosition and SetPosition
#
#
# Rect
#
# See GetRect and SetRect
#
#
# ScreenPosition
#
# See GetScreenPosition
#
#
# ScreenRect
#
# See GetScreenRect
#
#
# Shown
#
# See IsShown and Show
#
#
# Size
#
# See GetSize and SetSize
#
#
# Sizer
#
# See GetSizer and SetSizer
#
#
# ThemeEnabled
#
# See GetThemeEnabled and SetThemeEnabled
#
#
# ToolTip
#
# See GetToolTip and SetToolTip
#
#
# TopLevel
#
# See IsTopLevel
#
#
# TopLevelParent
#
# See GetTopLevelParent
#
#
# UpdateClientRect
#
# See GetUpdateClientRect
#
#
# UpdateRegion
#
# See GetUpdateRegion
#
#
# Validator
#
# See GetValidator and SetValidator
#
#
# VirtualSize
#
# See GetVirtualSize and SetVirtualSize
#
#
# WindowStyle
#
# See GetWindowStyle and SetWindowStyle
#
#
# WindowStyleFlag
#
# See GetWindowStyleFlag and SetWindowStyleFlag
#
#
# WindowVariant
#
# See GetWindowVariant and SetWindowVariant
#
# © Copyright 2012-2019, The wxPython Team. Created using Sphinx 1.4.5.
