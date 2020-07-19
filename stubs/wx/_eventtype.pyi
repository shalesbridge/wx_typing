from typing import NewType

# The wxpython docs mention a "wx.EventType", and mentions "wx.wxEVT_BUTTON" as an example; but so far I can't find an actual
# "wx.EventType" in Python.  Instead, it seems to just be "int"s.
EventType = NewType('EventType', int)


