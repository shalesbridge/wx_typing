import wx

class Event(wx.Object):
    """An event is a structure holding information about an event passed to a callback or member function.

    wx.Event used to be a multipurpose event object, and is an abstract base class for other event classes (see below).

    """

    def __init__(self, id=0, eventType: wx.EventType = wx.wxEVT_NULL) -> None:
        """Constructor.

        Notice that events are usually created by wxWidgets itself and creating e.g. a wx.PaintEvent in your code and sending it to e.g. a wx.TextCtrl will not usually affect it at all as native controls have no specific knowledge about wxWidgets events. However you may construct objects of specific types and pass them to wx.EvtHandler.ProcessEvent if you want to create your own custom control and want to process its events in the same manner as the standard ones.

        Also please notice that the order of parameters in this constructor is different from almost all the derived classes which specify the event type as the first argument.
        Parameters:

            id (int) – The identifier of the object (window, timer, ...) which generated this event.
            eventType (wx.EventType) – The unique type of event, e.g. wxEVT_PAINT , wxEVT_SIZE or wxEVT_BUTTON .
        """
        ...


    def Clone(self) -> Event:
        """Returns a copy of the event.

        Any event that is posted to the wxWidgets event system for later action (via wx.EvtHandler.AddPendingEvent , wx.EvtHandler.QueueEvent or wx.PostEvent ) must implement this method.

        All wxWidgets events fully implement this method, but any derived events implemented by the user should also implement this method just in case they (or some event derived from them) are ever posted.

        All wxWidgets events implement a copy constructor, so the easiest way of implementing the Clone function is to implement a copy constructor for a new event (call it MyEvent) and then define the Clone function like this:

        def Clone(self):

            return MyEvent()

        Return type:	wx.Event

        """
        ...


#     GetEventCategory(self)
#
#         Returns a generic category for this event.
#
#         wx.Event implementation returns wxEVT_CATEGORY_UI by default.
#
#         This function is used to selectively process events in wx.EventLoopBase.YieldFor .
#         Return type:	wx.EventCategory
#
#
#     GetEventObject(self)
#
#         Returns the object (usually a window) associated with the event, if any.
#         Return type:	wx.Object
#
#
#     GetEventType(self)
#
#         Returns the identifier of the given event type, such as wxEVT_BUTTON .
#         Return type:	wx.EventType
#
#
#     GetEventUserData(self)
#
#         Return the user data associated with a dynamically connected event handler.
#
#         wx.EvtHandler.Connect and wx.EvtHandler.Bind allow associating optional userData pointer with the handler and this method returns the value of this pointer.
#
#         The returned pointer is owned by wxWidgets and must not be deleted.
#         Return type:	wx.Object
#
#         New in version 2.9.5.
#
#
#     GetId(self)
#
#         Returns the identifier associated with this event, such as a button command id.
#         Return type:	int
#
#
#     GetSkipped(self)
#
#         Returns True if the event handler should be skipped, False otherwise.
#         Return type:	bool
#
#
#     GetTimestamp(self)
#
#         Gets the timestamp for the event.
#
#         The timestamp is the time in milliseconds since some fixed moment (not necessarily the standard Unix Epoch, so only differences between the timestamps and not their absolute values usually make sense).
#         Return type:	long
#
#         Warning
#
#         wxWidgets returns a not None timestamp only for mouse and key events (see wx.MouseEvent and wx.KeyEvent).
#
#
#     IsCommandEvent(self)
#
#         Returns True if the event is or is derived from wx.CommandEvent else it returns False.
#         Return type:	bool
#
#         Note
#
#         exists only for optimization purposes.
#
#
#     ResumePropagation(self, propagationLevel)
#
#         Sets the propagation level to the given value (for example returned from an earlier call to wx.Event.StopPropagation ).
#         Parameters:	propagationLevel (int) –
#
#
#     SetEventObject(self, object)
#
#         Sets the originating object.
#         Parameters:	object (wx.Object) –
#
#
#     SetEventType(self, type)
#
#         Sets the event type.
#         Parameters:	type (wx.EventType) –
#
#
#     SetId(self, id)
#
#         Sets the identifier associated with this event, such as a button command id.
#         Parameters:	id (int) –
#
#
#     SetTimestamp(self, timeStamp=0)
#
#         Sets the timestamp for the event.
#         Parameters:	timeStamp (long) –
#
#
#     ShouldPropagate(self)
#
#         Test if this event should be propagated or not, i.e. if the propagation level is currently greater than 0.
#         Return type:	bool
#
#
#     Skip(self, skip=True)
#
#         This method can be used inside an event handler to control whether further event handlers bound to this event will be called after the current one returns.
#
#         Without Skip (or equivalently if Skip(false) is used), the event will not be processed any more. If Skip(true) is called, the event processing system continues searching for a further handler function for this event, even though it has been processed already in the current handler.
#
#         In general, it is recommended to skip all non-command events to allow the default handling to take place. The command events are, however, normally not skipped as usually a single command such as a button click or menu item selection must only be processed by one handler.
#         Parameters:	skip (bool) –
#
#
#     StopPropagation(self)
#
#         Stop the event from propagating to its parent window.
#
#         Returns the old propagation level value which may be later passed to ResumePropagation to allow propagating the event again.
#         Return type:	int
#
#
#     Properties
#
#     EventObject
#
#         See GetEventObject and SetEventObject
#
#
#     EventType
#
#         See GetEventType and SetEventType
#
#
#     Id
#
#         See GetId and SetId
#
#
#     Skipped
#
#         See GetSkipped
#
#
#     Timestamp
#
#         See GetTimestamp and SetTimestamp
#
    ...
