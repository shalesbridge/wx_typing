from typing import overload, Any, NamedTuple, Text, Tuple, Union

import wx


class Colour(wx.Object):
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, red: int, green: int, blue: int, alpha: int = wx.ALPHA_OPAQUE) -> None:
        ...

    @overload
    def __init__ (self, colRGB: int) -> None:
        ...

    @overload
    def __init__(self, colour: Colour) -> None:
        ...

    def Alpha(self) -> int:
        ...

    @staticmethod
    def AlphaBlend(fg: int, bg: int, alpha: float) -> int:
        ...

    def Blue(self) -> int:
        ...

    @overload
    def ChangeLightness(self, ialpha: int) -> Colour:
        ...

    @overload
    def ChangeLightness(self, r: int, g: int, b: int, ialpha: int) -> Tuple[int, int, int]:
        ...

    def Get(self, includeAlpha: bool = True) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
        ...

    def GetAsString(self, flags: int = wx.C2S_NAME | wx.C2S_CSS_SYNTAX) -> Text:
        ...

    def GetIM(self) -> NamedTuple:
        ...

    def GetPixel(self) -> wx.IntPtr:
        ...

    # def GetRGB(self) -> wx.int:
    #     ...

    # def GetRGBA(self) -> wx.int:
    #     ...

    def GetRGB(self) -> int:
        ...

    def GetRGBA(self) -> int:
        ...

    def Green(self) -> int:
        ...

    def IsOk(self) -> bool:
        ...

    @overload
    def MakeDisabled(self, brightness: int) -> wx.Colour:
        ...

    @overload
    def MakeDisabled(self, r: int, g: int, b: int, brightness: int = 255) -> tuple[int, int, int]:
        ...

    @overload
    @staticmethod
    def MakeGrey(self, r: int, g: int, b: int) -> Tuple[int, int, int]:
        ...

    @overload
    @staticmethod
    def MakeGrey(self, r:int, g:int, b: int, weight_r: float, weight_g: float, weight_b: float) -> Tuple[int, int, int]:
        ...

    @staticmethod
    def MakeMono(on: bool) -> Tuple[int, int, int]:
        ...

    def Red(self) -> int:
        ...

    @overload
    def Set(self, red: int, green: int, blue: int, alpha: int = wx.ALPHA_OPAQUE) -> wx.Unknown:
        ...

    @overload
    def Set(self, RGB: int) -> wx.Unknown:
        ...

    @overload
    def Set(self, str: Text) -> bool:
        ...

    def SetRGB(self, colRGB: int) -> None:
    # def SetRGB(self, colRGB: wx.int) -> None:
        """Sets the RGB or RGBA colour values from a single 32 bit value.

        The arguments colRGB and colRGBA should be of the form 0x00BBGGRR and 0xAABBGGRR respectively where 0xRR , 0xGG , 0xBB and 0xAA are the values of the red, blue, green and alpha components.

        Notice the right-to-left order of components!
        Parameters:	colRGB (wx.int) –

        New in version 2.9.1.

        See also

        GetRGB , GetRGBA
        
        """
        ...


    def SetRGBA(self, colRGBA: int) -> None:
    # def SetRGBA(self, colRGBA: wx.int) -> None:
        """Sets the RGB or RGBA colour values from a single 32 bit value.

        The arguments colRGB and colRGBA should be of the form 0x00BBGGRR and 0xAABBGGRR respectively where 0xRR , 0xGG , 0xBB and 0xAA are the values of the red, blue, green and alpha components.

        Notice the right-to-left order of components!
        Parameters:	colRGBA (wx.int) –

        New in version 2.9.1.

        See also

        GetRGB , GetRGBA
        """
        ...

    def __bool__(self) -> int:
        ...

    # Currently not sure what the parameter or return types are.
    def __getitem__(self, idx: wx.Unknown) -> wx.Unknown:
        ...

    def __len__(self) -> int:
        ...

    def __nonzero__(self) -> int:
        ...

    # Currently not sure what the return type is.
    def __reduce__(self) -> wx.Unknown:
        ...

    # Currently not sure what the return type is.
    def __repr__(self) -> wx.Unknown:
        ...

    # Currently not sure what the parameter types or return type is.
    def __setitem__(self, idx: wx.Unknown, val: wx.Unknown) -> wx.Unknown:
        ...

    def __str__(self) -> Text:
        ...

    # _copyFrom(self, other)
    #
    #     For internal use only.

    # def __ne__(self):
    #
    #     Tests the inequality of two colours by comparing individual red, green, blue colours and alpha values.
    #     Parameters:	colour (wx.Colour) –

    # __eq__(self)
    #
    #     Tests the equality of two colours by comparing individual red, green, blue colours and alpha values.
    #     Parameters:	colour (wx.Colour) –


    Pixel: wx.IntPtr = ...

    # RGB: wx.int = ...
    #
    # RGBA: wx.int = ...

    RGB: int = ...

    RGBA: int = ...

    alpha: int = ...

    blue: int = ...

    green: int = ...

    red: int = ...
