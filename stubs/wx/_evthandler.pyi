from wx import Object, Trackable

class EvtHandler(Object, Trackable):
    #
    #     Possible constructors:
    #
    #     EvtHandler()
    #
    #     A class that can handle events from the windowing system.
    #
    #     Methods
    #
    #     __init__(self)
    #
    #         Constructor.
    #
    #
    #     static AddFilter(filter)
    #
    #         Add an event filter whose FilterEvent() method will be called for each and every event processed by wxWidgets.
    #
    #         The filters are called in LIFO order and wx.App is registered as an event filter by default. The pointer must remain valid until it’s removed with RemoveFilter and is not deleted by wx.EvtHandler.
    #         Parameters:	filter (wx.EventFilter) –
    #
    #         New in version 2.9.3.
    #
    #
    #     AddPendingEvent(self, event)
    #
    #         Post an event to be processed later.
    #
    #         This function is similar to wx.QueueEvent but can’t be used to post events from worker threads for the event objects with String fields (i.e. in practice most of them) because of an unsafe use of the same String object which happens because the String field in the original event object and its copy made internally by this function share the same string buffer internally. Use wx.QueueEvent to avoid this.
    #
    #         A copy of event is made by the function, so the original can be deleted as soon as function returns (it is common that the original is created on the stack). This requires that the wx.Event.Clone method be implemented by event so that it can be duplicated and stored until it gets processed.
    #         Parameters:	event (wx.Event) – Event to add to the pending events queue.
    #
    #
    #     Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
    #
    #         Bind an event to an event handler.
    #         Parameters:
    #
    #             event – One of the EVT_ event binder objects that specifies the type of event to bind.
    #             handler – A callable object to be invoked when the event is delivered to self. Pass None to disconnect an event handler.
    #             source – Sometimes the event originates from a different window than self, but you still want to catch it in self. (For example, a button event delivered to a frame.) By passing the source of the event, the event handling system is able to differentiate between the same event type from different controls.
    #             id – Used to spcify the event source by ID instead of instance.
    #             id2 – Used when it is desirable to bind a handler to a range of IDs, such as with EVT_MENU_RANGE.
    #
    #
    #     Connect(self, id, lastId, eventType, func)
    #
    #         Make an entry in the dynamic event table for an event binding.
    #
    #
    #     DeletePendingEvents(self)
    #
    #         Deletes all events queued on this event handler using wx.QueueEvent or AddPendingEvent .
    #
    #         Use with care because the events which are deleted are (obviously) not processed and this may have unwanted consequences (e.g. user actions events will be lost).
    #
    #
    #     Disconnect(self, id, lastId=-1, eventType=wxEVT_NULL, func=None)
    #
    #         Remove an event binding by removing its entry in the dynamic event table.
    #         Return type:	bool
    #
    #
    #     GetEvtHandlerEnabled(self)
    #
    #         Returns True if the event handler is enabled, False otherwise.
    #         Return type:	bool
    #
    #         See also
    #
    #         SetEvtHandlerEnabled
    #
    #
    #     GetNextHandler(self)
    #
    #         Returns the pointer to the next handler in the chain.
    #         Return type:	wx.EvtHandler
    #
    #         See also
    #
    #         SetNextHandler , GetPreviousHandler , SetPreviousHandler , wx.Window.PushEventHandler , wx.Window.PopEventHandler
    #
    #
    #     GetPreviousHandler(self)
    #
    #         Returns the pointer to the previous handler in the chain.
    #         Return type:	wx.EvtHandler
    #
    #         See also
    #
    #         SetPreviousHandler , GetNextHandler , SetNextHandler , wx.Window.PushEventHandler , wx.Window.PopEventHandler
    #
    #
    #     IsUnlinked(self)
    #
    #         Returns True if the next and the previous handler pointers of this event handler instance are None.
    #         Return type:	bool
    #
    #         New in version 2.9.0.
    #
    #         See also
    #
    #         SetPreviousHandler , SetNextHandler
    #
    #
    #     ProcessEvent(self, event)
    #
    #         Processes an event, searching event tables and calling zero or more suitable event handler function(s).
    #
    #         Normally, your application would not call this function: it is called in the wxWidgets implementation to dispatch incoming user interface events to the framework (and application).
    #
    #         However, you might need to call it if implementing new functionality (such as a new control) where you define new event types, as opposed to allowing the user to override virtual functions.
    #
    #         Notice that you don’t usually need to override wx.ProcessEvent to customize the event handling, overriding the specially provided TryBefore and TryAfter functions is usually enough. For example, wx.MDIParentFrame may override TryBefore to ensure that the menu events are processed in the active child frame before being processed in the parent frame itself.
    #
    #         The normal order of event table searching is as follows:
    #
    #             wx.App.FilterEvent is called. If it returns anything but -1 (default) the processing stops here.
    #             TryBefore is called (this is where wx.Validator are taken into account for wx.Window objects). If this returns True, the function exits.
    #             If the object is disabled (via a call to wx.EvtHandler.SetEvtHandlerEnabled ) the function skips to step (7).
    #             Dynamic event table of the handlers bound using Bind is searched. If a handler is found, it is executed and the function returns True unless the handler used wx.Event.Skip to indicate that it didn’t handle the event in which case the search continues.
    #             Static events table of the handlers bound using event table macros is searched for this event handler. If this fails, the base class event table is tried, and so on until no more tables exist or an appropriate function was found. If a handler is found, the same logic as in the previous step applies.
    #             The search is applied down the entire chain of event handlers (usually the chain has a length of one). This chain can be formed using wx.EvtHandler.SetNextHandler :
    #
    #         _images/overview_events_chain1.png
    #
    #             (referring to the image, if A->ProcessEvent is called and it doesn’t handle the event, B->ProcessEvent will be called and so on...). Note that in the case of wx.Window you can build a stack of event handlers (see wx.Window.PushEventHandler for more info). If any of the handlers of the chain return True, the function exits.
    #
    #             TryAfter is called: for the wx.Window object this may propagate the event to the window parent (recursively). If the event is still not processed, wx.ProcessEvent on TheApp object is called as the last step.
    #
    #         Notice that steps (2)-(6) are performed in ProcessEventLocally which is called by this function.
    #         Parameters:	event (wx.Event) – Event to process.
    #         Return type:	bool
    #         Returns:	True if a suitable event handler function was found and executed, and the function did not call wx.Event.Skip .
    #
    #         See also
    #
    #         SearchEventTable
    #
    #
    #     ProcessEventLocally(self, event)
    #
    #         Try to process the event in this handler and all those chained to it.
    #
    #         As explained in wx.ProcessEvent documentation, the event handlers may be chained in a doubly-linked list. This function tries to process the event in this handler (including performing any pre-processing done in TryBefore , e.g. applying validators) and all those following it in the chain until the event is processed or the chain is exhausted.
    #
    #         This function is called from wx.ProcessEvent and, in turn, calls TryBefore and TryAfter . It is not virtual and so cannot be overridden but can, and should, be called to forward an event to another handler instead of wx.ProcessEvent which would result in a duplicate call to TryAfter , e.g. resulting in all unprocessed events being sent to the application object multiple times.
    #         Parameters:	event (wx.Event) – Event to process.
    #         Return type:	bool
    #         Returns:	True if this handler of one of those chained to it processed the event.
    #
    #         New in version 2.9.1.
    #
    #
    #     ProcessPendingEvents(self)
    #
    #         Processes the pending events previously queued using wx.QueueEvent or AddPendingEvent ; you must call this function only if you are sure there are pending events for this handler, otherwise a CHECK will fail.
    #
    #         The real processing still happens in wx.ProcessEvent which is called by this function.
    #
    #         Note that this function needs a valid application object (see wx.AppConsole.GetInstance ) because wx.App holds the list of the event handlers with pending events and this function manipulates that list.
    #
    #
    #     QueueEvent(self, event)
    #
    #         Queue event for a later processing.
    #
    #         This method is similar to wx.ProcessEvent but while the latter is synchronous, i.e. the event is processed immediately, before the function returns, this one is asynchronous and returns immediately while the event will be processed at some later time (usually during the next event loop iteration).
    #
    #         Another important difference is that this method takes ownership of the event parameter, i.e. it will delete it itself. This implies that the event should be allocated on the heap and that the pointer can’t be used any more after the function returns (as it can be deleted at any moment).
    #
    #         wx.QueueEvent can be used for inter-thread communication from the worker threads to the main thread, it is safe in the sense that it uses locking internally and avoids the problem mentioned in AddPendingEvent documentation by ensuring that the event object is not used by the calling thread any more. Care should still be taken to avoid that some fields of this object are used by it, notably any String members of the event object must not be shallow copies of another String object as this would result in them still using the same string buffer behind the scenes. For example:
    #
    #         def FunctionInAWorkerThread(strs):
    #
    #             evt = wx.CommandEvent()
    #
    #             evt.SetString(strs)
    #
    #             wx.TheApp.QueueEvent(evt)
    #
    #         Note that you can use ThreadEvent instead of wx.CommandEvent to avoid this problem:
    #
    #         def FunctionInAWorkerThread(strs):
    #
    #             evt = wx.ThreadEvent()
    #             evt.SetString(strs)
    #
    #             # wx.ThreadEvent.Clone() makes sure that the internal wx.String
    #             # member is not shared by other string instances:
    #             wx.TheApp.QueueEvent(evt.Clone())
    #
    #         Finally notice that this method automatically wakes up the event loop if it is currently idle by calling wx.WakeUpIdle so there is no need to do it manually when using it.
    #         Parameters:	event (wx.Event) – A heap-allocated event to be queued, wx.QueueEvent takes ownership of it. This parameter shouldn’t be NULL .
    #
    #         New in version 2.9.0.
    #
    #
    #     static RemoveFilter(filter)
    #
    #         Remove a filter previously installed with AddFilter .
    #
    #         It’s an error to remove a filter that hadn’t been previously added or was already removed.
    #         Parameters:	filter (wx.EventFilter) –
    #
    #         New in version 2.9.3.
    #
    #
    #     SafelyProcessEvent(self, event)
    #
    #         Processes an event by calling wx.ProcessEvent and handles any exceptions that occur in the process.
    #
    #         If an exception is thrown in event handler, wx.App.OnExceptionInMainLoop is called.
    #         Parameters:	event (wx.Event) – Event to process.
    #         Return type:	bool
    #         Returns:	True if the event was processed, False if no handler was found or an exception was thrown.
    #
    #         See also
    #
    #         wx.Window.HandleWindowEvent
    #
    #
    #     SetEvtHandlerEnabled(self, enabled)
    #
    #         Enables or disables the event handler.
    #         Parameters:	enabled (bool) – True if the event handler is to be enabled, False if it is to be disabled.
    #
    #         Note
    #
    #         You can use this function to avoid having to remove the event handler from the chain, for example when implementing a dialog editor and changing from edit to test mode.
    #
    #         See also
    #
    #         GetEvtHandlerEnabled
    #
    #
    #     SetNextHandler(self, handler)
    #
    #         Sets the pointer to the next handler.
    #         Parameters:	handler (wx.EvtHandler) – The event handler to be set as the next handler. Cannot be None.
    #
    #         Note
    #
    #         See wx.ProcessEvent for more info about how the chains of event handlers are internally used. Also remember that wx.EvtHandler uses double-linked lists and thus if you use this function, you should also call SetPreviousHandler on the argument passed to this function:
    #
    #         handlerA.SetNextHandler(handlerB)
    #         handlerB.SetPreviousHandler(handlerA)
    #
    #         See also
    #
    #         How Events are Processed
    #
    #
    #     SetPreviousHandler(self, handler)
    #
    #         Sets the pointer to the previous handler.
    #
    #         All remarks about SetNextHandler apply to this function as well.
    #         Parameters:	handler (wx.EvtHandler) – The event handler to be set as the previous handler. Cannot be None.
    #
    #         See also
    #
    #         How Events are Processed
    #
    #
    #     TryAfter(self, event)
    #
    #         Method called by wx.ProcessEvent as last resort.
    #
    #         This method can be overridden to implement post-processing for the events which were not processed anywhere else.
    #
    #         The base class version handles forwarding the unprocessed events to wx.App at wx.EvtHandler level and propagating them upwards the window child-parent chain at wx.Window level and so should usually be called when overriding this method:
    #
    #         class MyClass(public BaseClass): # something inheriting from wx.EvtHandler
    #
    #         ...
    #             def TryAfter(self, event):
    #                 if (BaseClass.TryAfter(self, event))
    #                     return True
    #
    #                 return self.MyPostProcess(event)
    #
    #         Parameters:	event (wx.Event) –
    #         Return type:	bool
    #
    #         See also
    #
    #         wx.ProcessEvent
    #
    #
    #     TryBefore(self, event)
    #
    #         Method called by wx.ProcessEvent before examining this object event tables.
    #
    #         This method can be overridden to hook into the event processing logic as early as possible. You should usually call the base class version when overriding this method, even if wx.EvtHandler itself does nothing here, some derived classes do use this method, e.g. wx.Window implements support for wx.Validator in it.
    #
    #         Example:
    #
    #         class MyClass(BaseClass):  # something inheriting from wx.EvtHandler
    #
    #         ...
    #             def TryBefore(self, event):
    #                 if (self.MyPreProcess(event)):
    #                     return True
    #
    #                 return BaseClass.TryBefore(self, event)
    #
    #         Parameters:	event (wx.Event) –
    #         Return type:	bool
    #
    #         See also
    #
    #         wx.ProcessEvent
    #
    #
    #     Unbind(self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None)
    #
    #         Disconnects the event handler binding for event from self. Returns True if successful.
    #
    #
    #     Unlink(self)
    #
    #         Unlinks this event handler from the chain it’s part of (if any); then links the “previous” event handler to the “next” one (so that the chain won’t be interrupted).
    #
    #         E.g. if before calling Unlink you have the following chain:
    #         _images/evthandler_unlink_before.png
    #
    #             then after calling B-> Unlink you’ll have:
    #
    #         _images/evthandler_unlink_after.png
    #
    #         New in version 2.9.0.
    #
    #
    #     Properties
    #
    #     EvtHandlerEnabled
    #
    #         See GetEvtHandlerEnabled and SetEvtHandlerEnabled
    #
    #
    #     NextHandler
    #
    #         See GetNextHandler and SetNextHandler
    #
    #
    #     PreviousHandler
    #
    #         See GetPreviousHandler and SetPreviousHandler
    ...


