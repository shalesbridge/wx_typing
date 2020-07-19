from typing import Any, Optional, Text, Type

from wx._eventfilter import EventFilter
from wx._evthandler import EvtHandler


class AppConsole(EvtHandler, EventFilter):
#
#     This class is essential for writing console-only or hybrid apps without having to define USE_GUI=0.
#
#     Methods
#
#     DeletePendingEvents(self)
#
#         Deletes the pending events of all EvtHandlers of this application.
#
#         See wx.EvtHandler.DeletePendingEvents for warnings about deleting the pending events.
#
#
#     ExitMainLoop(self)
#
#         Call this to explicitly exit the main message (event) loop.
#
#         You should normally exit the main loop (and the application) by deleting the top window.
#
#         This function simply calls EvtLoopBase.Exit() on the active loop.
#
#
#     FilterEvent(self, event)
#
#         Overridden wx.EventFilter method.
#
#         This function is called before processing any event and allows the application to preempt the processing of some events, see wx.EventFilter documentation for more information.
#
#         wx.App implementation of this method always return -1 indicating that the event should be processed normally.
#         Parameters:	event (wx.Event) –
#         Return type:	int
#
#
#     GetAppDisplayName(self)
#
#         Returns the user-readable application name.
#
#         The difference between this string and the one returned by GetAppName is that this one is meant to be shown to the user and so should be used for the window titles, page headers and so on while the other one should be only used internally, e.g. for the file names or configuration file keys.
#
#         If the application name for display had been previously set by SetAppDisplayName , it will be returned by this function. Otherwise, if SetAppName had been called its value will be returned; also as is. Finally if none was called, this function returns the program name capitalized using String.Capitalize .
#         Return type:	string
#
#         New in version 2.9.0.
#
#
#     GetAppName(self)
#
#         Returns the application name.
#
#         If SetAppName had been called, returns the string passed to it. Otherwise returns the program name, i.e. the value of argv [0] passed to the main() function.
#         Return type:	string
#
#         See also
#
#         GetAppDisplayName
#
#
#     GetClassName(self)
#
#         Gets the class name of the application.
#
#         The class name may be used in a platform specific manner to refer to the application.
#         Return type:	string
#
#         See also
#
#         SetClassName
#
#
#     static GetInstance()
#
#         Returns the one and only global application object.
#
#         Usually wx.TheApp is used instead.
#         Return type:	wx.AppConsole
#
#         See also
#
#         SetInstance
#
#
#     GetMainLoop(self)
#
#         Returns the main event loop instance, i.e. the event loop which is started by OnRun and which dispatches all events sent from the native toolkit to the application (except when new event loops are temporarily set-up).
#
#         The returned value maybe None. Put initialization code which needs a not None main event loop into OnEventLoopEnter .
#         Return type:	wx.EventLoopBase
#
#
#     GetTraits(self)
#
#         Returns a pointer to the wx.AppTraits object for the application.
#
#         If you want to customize the wx.AppTraits object, you must override the CreateTraits function.
#         Return type:	wx.AppTraits
#
#
#     GetVendorDisplayName(self)
#
#         Returns the user-readable vendor name.
#
#         The difference between this string and the one returned by GetVendorName is that this one is meant to be shown to the user and so should be used for the window titles, page headers and so on while the other one should be only used internally, e.g. for the file names or configuration file keys.
#
#         By default, returns the same string as GetVendorName .
#         Return type:	string
#
#         New in version 2.9.0.
#
#
#     GetVendorName(self)
#
#         Returns the application’s vendor name.
#         Return type:	string
#
#
#     HasPendingEvents(self)
#
#         Returns True if there are pending events on the internal pending event list.
#
#         Whenever wx.EvtHandler.QueueEvent or wx.EvtHandler.AddPendingEvent are called (not only for wx.App itself, but for any event handler of the application!), the internal wx.App‘s list of handlers with pending events is updated and this function will return True.
#         Return type:	bool
#
#
#     static IsMainLoopRunning()
#
#         Returns True if the main event loop is currently running, i.e. if the application is inside OnRun .
#
#         This can be useful to test whether events can be dispatched. For example, if this function returns False, non-blocking sockets cannot be used because the events from them would never be processed.
#         Return type:	bool
#
#
#     IsScheduledForDestruction(self, object)
#
#         Check if the object had been scheduled for destruction with ScheduleForDestruction .
#
#         This function may be useful as an optimization to avoid doing something with an object which will be soon destroyed in any case.
#         Parameters:	object (wx.Object) –
#         Return type:	bool
#
#
#     MainLoop(self)
#
#         Called by wxWidgets on creation of the application.
#
#         Override this if you wish to provide your own (environment-dependent) main loop.
#         Return type:	int
#         Returns:	0 under X, and the wParam of the WM_QUIT message under Windows.
#
#
#     OnEventLoopEnter(self, loop)
#
#         Called by wx.EventLoopBase.SetActive : you can override this function and put here the code which needs an active event loop.
#
#         Note that this function is called whenever an event loop is activated; you may want to use wx.EventLoopBase.IsMain to perform initialization specific for the app’s main event loop.
#         Parameters:	loop (wx.EventLoopBase) –
#
#         See also
#
#         OnEventLoopExit
#
#
#     OnEventLoopExit(self, loop)
#
#         Called by wx.EventLoopBase.OnExit for each event loop which is exited.
#         Parameters:	loop (wx.EventLoopBase) –
#
#         See also
#
#         OnEventLoopEnter
#
#
#     OnExit(self)
#
#         Override this member function for any processing which needs to be done as the application is about to exit.
#
#         OnExit is called after destroying all application windows and controls, but before wxWidgets cleanup. Note that it is not called at all if OnInit failed.
#
#         The return value of this function is currently ignored, return the same value as returned by the base class method if you override it.
#         Return type:	int
#
#
#     OnInit(self)
#
#         This must be provided by the application, and will usually create the application’s main window, optionally calling SetTopWindow().
#
#         You may use OnExit to clean up anything initialized here, provided that the function returns True.
#
#         Notice that if you want to use the command line processing provided by wxWidgets you have to call the base class version in the derived class OnInit .
#
#         Return True to continue processing, False to exit the application immediately.
#         Return type:	bool
#
#
#     OnRun(self)
#
#         This virtual function is where the execution of a program written in wxWidgets starts.
#
#         The default implementation just enters the main loop and starts handling the events until it terminates, either because ExitMainLoop has been explicitly called or because the last frame has been deleted and GetExitOnFrameDelete() flag is True (this is the default).
#
#         The return value of this function becomes the exit code of the program, so it should return 0 in case of successful termination.
#         Return type:	int
#
#
#     ProcessPendingEvents(self)
#
#         Process all pending events; it is necessary to call this function to process events posted with wx.EvtHandler.QueueEvent or wx.EvtHandler.AddPendingEvent .
#
#         This happens during each event loop iteration (see wx.EventLoopBase) in GUI mode but it may be also called directly.
#
#         Note that this function does not only process the pending events for the wx.App object itself (which derives from wx.EvtHandler) but also the pending events for any event handler of this application.
#
#         This function will immediately return and do nothing if SuspendProcessingOfPendingEvents was called.
#
#
#     ResumeProcessingOfPendingEvents(self)
#
#         Resume processing of the pending events previously stopped because of a call to SuspendProcessingOfPendingEvents .
#
#
#     ScheduleForDestruction(self, object)
#
#         Delayed objects destruction.
#
#         In applications using events it may be unsafe for an event handler to delete the object which generated the event because more events may be still pending for the same object. In this case the handler may call ScheduleForDestruction instead. Schedule the object for destruction in the near future.
#
#         Notice that if the application is not using an event loop, i.e. if UsesEventLoop returns False, this method will simply delete the object immediately.
#
#         Examples of using this function inside wxWidgets itself include deleting the top level windows when they are closed and sockets when they are disconnected.
#         Parameters:	object (wx.Object) –
#
#
#     SetAppDisplayName(self, name)
#
#         Set the application name to be used in the user-visible places such as window titles.
#
#         See GetAppDisplayName for more about the differences between the display name and name.
#
#         Notice that if this function is called, the name is used as is, without any capitalization as done by default by GetAppDisplayName .
#         Parameters:	name (string) –
#
#
#     SetAppName(self, name)
#
#         Sets the name of the application.
#
#         This name should be used for file names, configuration file entries and other internal strings. For the user-visible strings, such as the window titles, the application display name set by SetAppDisplayName is used instead.
#
#         By default the application name is set to the name of its executable file.
#         Parameters:	name (string) –
#
#         See also
#
#         GetAppName
#
#
#     SetCLocale(self)
#
#         Sets the C locale to the default locale for the current environment.
#
#         It is advised to call this to ensure that the underlying toolkit uses the locale in which the numbers and monetary amounts are shown in the format expected by user and so on.
#
#         Calling this function is roughly equivalent to calling
#
#         setlocale(LC_ALL, "")
#
#         but performs additional toolkit-specific tasks under some platforms and so should be used instead of setlocale() itself. Alternatively, you can use wx.Locale to change the locale with more control.
#
#         Notice that this does not change the global C++ locale, you need to do it explicitly if you want, e.g.
#
#         but be warned that locale support in C++ standard library can be poor or worse under some platforms, e.g. the above line results in an immediate crash under OS X up to the version 10.8.2.
#
#         New in version 2.9.5.
#
#
#     SetClassName(self, name)
#
#         Sets the class name of the application.
#
#         This may be used in a platform specific manner to refer to the application.
#         Parameters:	name (string) –
#
#         See also
#
#         GetClassName
#
#
#     static SetInstance(app)
#
#         Allows external code to modify global wx.TheApp , but you should really know what you’re doing if you call it.
#         Parameters:	app (wx.AppConsole) – Replacement for the global application object.
#
#         See also
#
#         GetInstance
#
#
#     SetVendorDisplayName(self, name)
#
#         Set the vendor name to be used in the user-visible places.
#
#         See GetVendorDisplayName for more about the differences between the display name and name.
#         Parameters:	name (string) –
#
#
#     SetVendorName(self, name)
#
#         Sets the name of application’s vendor.
#
#         The name will be used in registry access. A default name is set by wxWidgets.
#         Parameters:	name (string) –
#
#         See also
#
#         GetVendorName
#
#
#     SuspendProcessingOfPendingEvents(self)
#
#         Temporary suspends processing of the pending events.
#
#         See also
#
#         ResumeProcessingOfPendingEvents
#
#
#     Yield(self, onlyIfNeeded=False)
#         Parameters:	onlyIfNeeded (bool) –
#         Return type:	bool
#
#
#     Properties
#
#     AppDisplayName
#
#         See GetAppDisplayName and SetAppDisplayName
#
#
#     AppName
#
#         See GetAppName and SetAppName
#
#
#     ClassName
#
#         See GetClassName and SetClassName
#
#
#     Traits
#
#         See GetTraits
#
#
#     VendorDisplayName
#
#         See GetVendorDisplayName and SetVendorDisplayName
#
#
#     VendorName
#
#         See GetVendorName and SetVendorName
    ...


class PyApp(AppConsole):

#     Possible constructors:
#
#     PyApp()
#
#     The App class represents the application itself when USE_GUI=1.
#
#     Methods
#
#     __init__(self)
#
#         Constructor.
#
#         Called implicitly with a definition of a wx.App object.
#
#
#     GetAssertMode(self)
#
#         Returns the current mode for how the application responds to asserts.
#         Return type:	wx.AppAssertMode
#
#
#     static GetComCtl32Version()
#
#             Returns 400, 470, 471, etc. for comctl32.dll 4.00, 4.70, 4.71 or 0 if it wasn’t found at all. Raises an exception on non-Windows platforms.
#
#         Return type:	int
#
#
#     GetDisplayMode(self)
#
#         Get display mode that is used use.
#
#         This is only used in framebuffer wxWidgets ports such as wxDFB.
#         Return type:	wx.VideoMode
#
#
#     GetExitOnFrameDelete(self)
#
#         Returns True if the application will exit when the top-level frame is deleted.
#         Return type:	bool
#
#         See also
#
#         SetExitOnFrameDelete
#
#
#     GetLayoutDirection(self)
#
#         Return the layout direction for the current locale or Layout_Default if it’s unknown.
#         Return type:	wx.LayoutDirection
#
#
#     static GetShell32Version()
#
#             Returns 400, 470, 471, etc. for shell32.dll 4.00, 4.70, 4.71 or 0 if it wasn’t found at all. Raises an exception on non-Windows platforms.
#
#         Return type:	int
#
#
#     GetTopWindow(self)
#
#         Returns a pointer to the top window.
#         Return type:	wx.Window
#
#         Note
#
#         If the top window hasn’t been set using SetTopWindow , this function will find the first top-level window (frame or dialog or instance of wx.TopLevelWindow) from the internal top level window list and return that.
#
#         See also
#
#         SetTopWindow
#
#
#     GetUseBestVisual(self)
#
#         Returns True if the application will use the best visual on systems that support different visuals, False otherwise.
#         Return type:	bool
#
#         See also
#
#         SetUseBestVisual
#
#
#     IsActive(self)
#
#         Returns True if the application is active, i.e. if one of its windows is currently in the foreground.
#
#         If this function returns False and you need to attract users attention to the application, you may use wx.TopLevelWindow.RequestUserAttention to do it.
#         Return type:	bool
#
#
#     static IsDisplayAvailable()
#
#             Returns True if the application is able to connect to the system’s display, or whatever the equivallent is for the platform.
#
#         Return type:	bool
#
#
#     MacHideApp(self)
#
#         Hide all application windows just as the user can do with the system Hide command. Mac only.
#
#
#     MacNewFile(self)
#
#         Called in response of an “open-application” Apple event.
#
#         Override this to create a new document in your app.
#
#         Availability
#
#         Only available for OSX.
#
#
#     MacOpenFile(self, fileName)
#
#         Called in response of an “open-document” Apple event.
#         Parameters:	fileName (string) –
#
#         Deprecated
#
#         This function is kept mostly for backwards compatibility. Please override wx.App.MacOpenFiles method instead in any new code.
#
#         Availability
#
#         Only available for OSX.
#
#
#     MacOpenFiles(self, fileNames)
#
#         Called in response of an openFiles message with Cocoa, or an “open-document” Apple event with Carbon.
#
#         You need to override this method in order to open one or more document files after the user double clicked on it or if the files and/or folders were dropped on either the application in the dock or the application icon in Finder.
#
#         By default this method calls MacOpenFile for each file/folder.
#         Parameters:	fileNames (list of strings) –
#
#         New in version 2.9.3.
#
#         Availability
#
#         Only available for OSX.
#
#
#     MacOpenURL(self, url)
#
#         Called in response of a “get-url” Apple event.
#         Parameters:	url (string) –
#
#         Availability
#
#         Only available for OSX.
#
#
#     MacPrintFile(self, fileName)
#
#         Called in response of a “print-document” Apple event.
#         Parameters:	fileName (string) –
#
#         Availability
#
#         Only available for OSX.
#
#
#     MacReopenApp(self)
#
#         Called in response of a “reopen-application” Apple event.
#
#         Availability
#
#         Only available for OSX.
#
#
#     OSXIsGUIApplication(self)
#
#         May be overridden to indicate that the application is not a foreground GUI application under OS X.
#
#         This method is called during the application startup and returns True by default. In this case, wxWidgets ensures that the application is ran as a foreground, GUI application so that the user can interact with it normally, even if it is not bundled. If this is undesired, i.e. if the application doesn’t need to be brought to the foreground, this method can be overridden to return False.
#
#         Notice that overriding it doesn’t make any difference for the bundled applications which are always foreground unless LSBackgroundOnly key is specified in the Info.plist file.
#         Return type:	bool
#
#         New in version 3.0.1.
#
#         Availability
#
#         Only available for OSX.
#
#
#     SafeYield(self, win, onlyIfNeeded)
#
#         This function is similar to wx.Yield , except that it disables the user input to all program windows before calling wx.AppConsole.Yield and re-enables it again afterwards.
#
#         If win is not None, this window will remain enabled, allowing the implementation of some limited user interaction. Returns the result of the call to wx.AppConsole.Yield .
#         Parameters:
#
#             win (wx.Window) –
#             onlyIfNeeded (bool) –
#
#         Return type:
#
#         bool
#
#         See also
#
#         wx.SafeYield
#
#
#     SafeYieldFor(self, win, eventsToProcess)
#
#         Works like wx.SafeYield with onlyIfNeeded == True except that it allows the caller to specify a mask of events to be processed.
#
#         See AppConsole.YieldFor for more info.
#         Parameters:
#
#             win (wx.Window) –
#             eventsToProcess (long) –
#
#         Return type:
#
#         bool
#
#
#     SetAssertMode(self, AppAssertMode)
#
#             Set the mode indicating how the application responds to assertion statements. Valid settings are a combination of these flags:
#
#                     wx.``wx.APP_ASSERT_SUPPRESS``
#                     wx.``wx.APP_ASSERT_EXCEPTION``
#                     wx.``wx.APP_ASSERT_DIALOG``
#                     wx.``wx.APP_ASSERT_LOG``
#
#             The default behavior is to raise a wx.wxAssertionError exception.
#
#         Parameters:	wxAppAssertMode (AppAssertMode) –
#
#
#     SetDisplayMode(self, info)
#
#         Set display mode to use.
#
#         This is only used in framebuffer wxWidgets ports such as wxDFB.
#         Parameters:	info (wx.VideoMode) –
#         Return type:	bool
#
#
#     SetExitOnFrameDelete(self, flag)
#
#         Allows the programmer to specify whether the application will exit when the top-level frame is deleted.
#         Parameters:	flag (bool) – If True (the default), the application will exit when the top-level frame is deleted. If False, the application will continue to run.
#
#         See also
#
#         GetExitOnFrameDelete , Application Shutdown
#
#
#     SetNativeTheme(self, theme)
#
#         Allows runtime switching of the UI environment theme.
#
#         Currently implemented for GTK2-only. Return True if theme was successfully changed.
#         Parameters:	theme (string) – The name of the new theme or an absolute path to a gtkrc-theme-file
#         Return type:	bool
#
#
#     SetTopWindow(self, window)
#
#         Sets the ‘top’ window.
#
#         You can call this from within OnInit to let wxWidgets know which is the main window. You don’t have to set the top window; it is only a convenience so that (for example) certain dialogs without parents can use a specific window as the top window.
#
#         If no top window is specified by the application, wxWidgets just uses the first frame or dialog (or better, any wx.TopLevelWindow) in its top-level window list, when it needs to use the top window. If you previously called SetTopWindow and now you need to restore this automatic behaviour you can call:
#
#         wx.App.SetTopWindow(None)
#
#         Parameters:	window (wx.Window) – The new top window.
#
#         See also
#
#         GetTopWindow , OnInit
#
#
#     SetUseBestVisual(self, flag, forceTrueColour=False)
#
#         Allows the programmer to specify whether the application will use the best visual on systems that support several visual on the same display.
#
#         This is typically the case under Solaris and IRIX, where the default visual is only 8-bit whereas certain applications are supposed to run in TrueColour mode.
#
#         Note that this function has to be called in the constructor of the wx.App instance and won’t have any effect when called later on. This function currently only has effect under GTK.
#         Parameters:
#
#             flag (bool) – If True, the app will use the best visual.
#             forceTrueColour (bool) – If True then the application will try to force using a TrueColour visual and abort the app if none is found.
#
#
#     Properties
#
#     AssertMode
#
#         See GetAssertMode and SetAssertMode
#
#
#     DisplayMode
#
#         See GetDisplayMode and SetDisplayMode
#
#
#     ExitOnFrameDelete
#
#         See GetExitOnFrameDelete and SetExitOnFrameDelete
#
#
#     LayoutDirection
#
#         See GetLayoutDirection
#
#
#     TopWindow
#
#         See GetTopWindow and SetTopWindow
#
#
#     UseBestVisual
#
#         See GetUseBestVisual and SetUseBestVisual
    ...


class App(PyApp):
    """The wx.App class represents the application and is used to:

            bootstrap the wxPython system and initialize the underlying gui toolkit
            set and get application-wide properties
            implement the native windowing system main message or event loop, and to dispatch events to window instances
            etc.

    Every wx application must have a single wx.App instance, and all creation of UI objects should be delayed until after the wx.App object has been created in order to ensure that the gui platform and wxWidgets have been fully initialized.

    Normally you would derive from this class and implement an OnInit method that creates a frame and then calls self.SetTopWindow(frame), however wx.App is also usable on it’s own without derivation.

    """
    def __init__(self, redirect: bool = False, filename: Optional[Text] = None, useBestVisual: bool = False, clearSigInt: bool = True) -> None:
        """Construct a wx.App object.
        Parameters:

            redirect – Should sys.stdout and sys.stderr be redirected? Defaults to False. If filename is None then output will be redirected to a window that pops up as needed. (You can control what kind of window is created for the output by resetting the class variable outputWindowClass to a class of your choosing.)
            filename – The name of a file to redirect output to, if redirect is True.
            useBestVisual – Should the app try to use the best available visual provided by the system (only relevant on systems that have more than one visual.) This parameter must be used instead of calling SetUseBestVisual later on because it must be set before the underlying GUI toolkit is initialized.
            clearSigInt – Should SIGINT be cleared? This allows the app to terminate upon a Ctrl-C in the console like other GUI apps will.

        Note

        You should override OnInit to do application initialization to ensure that the system, toolkit and wxWidgets are fully initialized.

        """
        ...


#     @staticmethod
#     def Get(self):
#         """A staticmethod returning the currently active application object. Essentially just a more pythonic version of GetApp.
#
#         """
#         ...

    def MainLoop(self) -> None:
        """Execute the main GUI event loop

        """
        ...

    def OnPreInit(self) -> None:
        """Things that must be done after _BootstrapApp has done its thing, but would be nice if they were already done by the time that OnInit is called. This can be overridden in derived classes, but be sure to call this method from there.

        """
        ...

    def RedirectStdio(self, filename: Optional[Text] = None) -> None:
        """Redirect sys.stdout and sys.stderr to a file or a popup window.

        """
        ...

    def RestoreStdio(self) -> None:
        ...

    def SetOutputWindowAttributes(self, title: Optional[Text] = None, pos: Optional[Any] = None, size: Optional[Any] = None):
        """Set the title, position and/or size of the output window if the stdio has been redirected. This should be called before any output would cause the output window to be created.

        """
        ...

    def SetTopWindow(self, frame: Any) -> None:
        """Set the “main” top level window, which will be used for the parent of the on-demand output window as well as for dialogs that do not have an explicit parent set.

        """
        ...

    def __del__(self) -> None:
        ...