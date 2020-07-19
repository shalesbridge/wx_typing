import logging
from typing import Any, MutableMapping, Optional, Text, Type

import wx
# import wx.dataview as dv

import data as _data

class DataViewItem(object):
    """DataViewItem is a small opaque class that represents an item in a DataViewCtrl in a persistent way, i.e.

    """

    def __init__(self, *args, **kw) -> None:
        """Constructor.

        overload Overloaded Implementations:

        __init__ (self)

        __init__ (self, item)
        Parameters:	item (wx.dataview.DataViewItem) –

        __init__ (self, id)
        Parameters:	id –

        """

    def GetID(self) -> Any:
        """Returns the ID.

        """
        ...

    def IsOk(self) -> bool:
        """Returns True if the ID is not None.

        """
        ...

    def __bool__(self) -> int:
        """
        Return type:	int

        """
        ...

    def __eq__(self, other: Any) -> bool:
        """Return type:	bool

        """
        ...

    def __hash__(self) -> int:
        """Return type:	long

        """
        ...

    def __ne__(self, other: Any) -> bool:
        """Return type: bool

        """
        ...

    def __nonzero__(self):
        """Return type: int

        """
        ...

    ID: Any

