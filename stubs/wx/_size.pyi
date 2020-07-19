import collections
from typing import overload, Any, NamedTuple, Text, Tuple

import wx

class Size(object):
    @overload
    def __init__(self) -> None:
        """overload Overloaded Implementations:


        __init__ (self)

        Initializes this size object with zero width and height.


        __init__ (self, width, height)

        Initializes this size object with the given width and height.
        Parameters:

            width (int) –
            height (int) –

        """
        ...

    @overload
    def __init__(self, width: int, height: int) -> None:
        ...

    @overload
    def DecBy(self, pt: wx.Point) -> wx.Unknown:
        """Decreases the size in both x and y directions.

        See also

        IncBy

        overload Overloaded Implementations:


        DecBy (self, pt)
        Parameters:	pt (wx.Point) –


        DecBy (self, size)
        Parameters:	size (wx.Size) –


        DecBy (self, dx, dy)
        Parameters:

            dx (int) –
            dy (int) –


        DecBy (self, d)
        Parameters:	d (int) –
        """
        ...

    @overload
    def DecBy(self, size: Size) -> wx.Unknown:
        ...

    @overload
    def DecBy(self, dx: int, dy: int) -> wx.Unknown:
        ...

    @overload
    def DecBy(self, d: int) -> wx.Unknown:
        ...

    def DecTo(self, size: Size) -> wx.Unknown:
        ...

    def DecToIfSpecified(self, size: Size) -> wx.Unknown:
        ...

    def Get(self) -> Tuple:
        ...

    def GetHeight(self) -> int:
        ...

    def GetIM(self) -> NamedTuple:
        ...

    def GetWidth(self) -> int:
        ...

    def IncBy(self, *args, **kw) -> Any:
        """Increases the size in both x and y directions.

        See also

        DecBy

        overload Overloaded Implementations:


        IncBy (self, pt)
        Parameters:	pt (wx.Point) –


        IncBy (self, size)
        Parameters:	size (wx.Size) –


        IncBy (self, dx, dy)
        Parameters:

            dx (int) –
            dy (int) –


        IncBy (self, d)
        Parameters:	d (int) –

        """
        ...

    def IncTo(self, size: Size) -> wx.Unknown:
        ...

    def IsFullySpecified(self) -> bool:
        ...

    def Scale(self, xscale: float, yscale: float) -> Size:
        ...

    def Set(self, width: int, height: int) -> wx.Unknown:
        ...

    def SetDefaults(self, sizeDefault: Size) -> wx.Unknown:
        ...

    def SetHeight(self, height: int) -> wx.Unknown:
        ...

    def SetWidth(self, width) -> wx.Unknown:
        ...

    def __getitem__(self, idx: wx.Unknown) -> wx.Unknown:
        ...

    def __len__(self) -> int:
        ...

#     __ne__(self, other)
#         Return type:	bool
#
#
#     __nonzero__(self)
#
#
#     __reduce__(self)
#
#
#     __repr__(self)


    def __setitem__(self, idx: wx.Unknown, val: wx.Unknown) -> wx.Unknown:
        ...

    def __str__(self) -> Text:
        ...

#     __imul__(self)
#         Parameters:	factor (int) –


#     __iadd__(self)
#         Parameters:	sz (wx.Size) –
#
#
#     __isub__(self)
#         Parameters:	sz (wx.Size) –
#
#
#     __idiv__(self)
#         Parameters:	factor (int) –

    Height: int

    Width: int

    height: int

    width: int

    x: int

    y: int

DefaultSize: Size = Size(-1, -1)
