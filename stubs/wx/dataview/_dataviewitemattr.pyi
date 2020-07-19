import wx

class DataViewItemAttr(object):
    """This class is used to indicate to a DataViewCtrl that a certain item (see DataViewItem) has extra font attributes for its renderer.

    """
    ...
    def __init__(self) -> None:
        """Constructor.

        """
        ...

    def GetBackgroundColour(self) -> wx.Colour:
        """Returns the colour to be used for the background.
        Return type:	Colour

        """
        ...

    def GetBold(self) -> bool:
        """Returns value of the bold property.
        Return type:	bool

        """
        ...

    def GetColour(self) -> wx.Colour:
        """Returns this attribute’s colour.
        Return type:	Colour

        """
        ...

    def GetEffectiveFont(self, font: wx.Font) -> wx.Font:
        """Return the font based on the given one with this attribute applied to it.
        Parameters:	font (wx.Font) –
        Return type:	Font

        """
        ...

    def GetItalic(self) -> bool:
        """Returns value of the italics property.
        Return type:	bool

        """
        ...

    def HasBackgroundColour(self) -> bool:
        """Returns True if the background colour property has been set.
        Return type:	bool

        """
        ...

    def HasColour(self) -> bool:
        """Returns True if the colour property has been set.
        Return type:	bool

        """
        ...

    def HasFont(self) -> bool:
        """Returns True if any property affecting the font has been set.
        Return type:	bool

        """
        ...

    def IsDefault(self) -> bool:
        """Returns True if none of the properties have been set.
        Return type:	bool

        """
        ...

    def SetBackgroundColour(self, colour: wx.Colour) -> None:
        """Call this to set the background colour to use.

        Currently this attribute is only supported in the generic version of wx.dataview.DataViewCtrl and ignored by the native GTK+ and OS X implementations.
        Parameters:	colour (wx.Colour) –

        New in version 2.9.4.

        """
        ...

    def SetBold(self, set: bool) -> None:
        """Call this to indicate that the item shall be displayed in bold text.
        Parameters:	set (bool) –

        """
        ...

    def SetColour(self, colour: wx.Colour) -> None:
        """Call this to indicate that the item shall be displayed with that colour.
        Parameters:	colour (wx.Colour) –

        """
        ...

    def SetItalic(self, set: bool) -> None:
        """Call this to indicate that the item shall be displayed in italic text.
        Parameters:	set (bool) –

        """
        ...

    BackgroundColour: wx.Colour = ...

    Bold: bool = ...

    Colour: wx.Colour = ...

    Italic: bool = ...
