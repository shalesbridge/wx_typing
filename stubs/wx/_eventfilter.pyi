from typing import Any

from wx import Event


class EventFilter(object):
    """A global event filter for pre-processing all the events generated in the program.

    This is a very simple class which just provides FilterEvent virtual method to be called by wx.EvtHandler before starting process of any event. Thus, inheriting from this class and overriding FilterEvent allows to capture and possibly handle or ignore all the events happening in the program. Of course, having event filters adds additional overhead to every event processing and so should not be used lightly and your FilterEvent code should try to return as quickly as possible, especially for the events it is not interested in.

    An example of using this class:

    # This class allows to determine the last time the user has worked with
    # this application:
    class LastActivityTimeDetector(wx.EventFilter):

        def __init__(self):

            wx.EventFilter.__init__(self)

            wx.EvtHandler.AddFilter(self)

            self.last = wx.DateTime.Now()


        def __del__(self):

            wx.EvtHandler.RemoveFilter(self)


        def FilterEvent(self, event):

            # Update the last user activity
            t = event.GetEventType()

            if t == wx.EVT_KEY_DOWN.typeId or t == wx.EVT_MOTION.typeId or \
               t == wx.EVT_LEFT_DOWN.typeId or t == wx.EVT_RIGHT_DOWN.typeId or \
               t == wx.EVT_MIDDLE_DOWN.typeId:

                self.last = wx.DateTime.Now()


            # Continue processing the event normally as well.
            return self.Event_Skip


        # This function could be called periodically from some timer to
        # do something (e.g. hide sensitive data or log out from remote
        # server) if the user has been inactive for some time period.
        def IsInactiveFor(self, diff):

            return wx.DateTime.Now() - diff > self.last

    Notice that wx.App derives from wx.EventFilter and is registered as an event filter during its creation so you may also override FilterEvent method in your App-derived class and, in fact, this is often the most convenient way to do it. However creating a new class deriving directly from wx.EventFilter allows to isolate the event filtering code in its own separate class and also to have several independent filters, if necessary.

    New in version 2.9.3.

    """

    def __init__(self) -> None:
        """Default constructor.

        Constructor does not register this filter using wx.EvtHandler.AddFilter , it’s your responsibility to do it when necessary.

        Notice that the objects of this class can’t be copied.

        """
        ...

    def FilterEvent(self, event: Event) -> int:
        """Override this method to implement event pre-processing.

        This method allows to filter all the events processed by the program, so you should try to return quickly from it to avoid slowing down the program to a crawl.

        Although the return type of this method is int , this is only due to backwards compatibility concerns and the actual return value must be one of the Event_XXX constants defined above:

            Event_Skip to continue processing the event normally (this should be used in most cases).
            Event_Ignore to not process this event at all (this can be used to suppress some events).
            Event_Processed to not process this event normally but indicate that it was already processed by the event filter and so no default processing should take place neither (this should only be used if the filter really did process the event).

        Parameters:	event (wx.Event) –
        Return type:	int

        """
        ...
