from typing import overload


class Object(object):
    """This is the root class of many of the wxWidgets classes.

    It declares a virtual destructor which ensures that destructors get called for all derived class objects where necessary.

    wx.Object is the hub of a dynamic object creation scheme, enabling a program to create instances of a class only knowing its string class name, and to query the class hierarchy.

    The class contains optional debugging versions of new and delete, which can help trace memory allocation and deallocation problems.

    wx.Object can be used to implement reference counted objects, such as wx.Pen, wx.Bitmap and others (see this list). See wx.RefCounter and Reference Counting for more info about reference counting.

    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, other: Object) -> None:
        ...


    #     Destroy(self)
    #
    #         Deletes the C++ object this Python object is a proxy for.
    #
    #
    #     GetClassInfo(self)
    #
    #         This virtual function is redefined for every class that requires run-time type information, when using the DECLARE_CLASS macro (or similar).
    #         Return type:	wx.ClassInfo
    #
    #
    #     GetClassName(self)
    #
    #         Returns the class name of the C++ class using RTTI.
    #         Return type:	wx.Char
    #
    #
    #     GetRefData(self)
    #
    #         Returns the Object.m_refData pointer, i.e. the data referenced by this object.
    #         Return type:	wx.ObjectRefData
    #
    #         See also
    #
    #         Ref , UnRef , Object.m_refData, SetRefData , wx.ObjectRefData
    #
    #
    #     IsSameAs(self, obj)
    #
    #         Returns True if this object has the same data pointer as obj.
    #
    #         Notice that True is returned if the data pointers are None in both objects.
    #
    #         This function only does a shallow comparison, i.e. it doesn’t compare the objects pointed to by the data pointers of these objects.
    #         Parameters:	obj (wx.Object) –
    #         Return type:	bool
    #
    #         See also
    #
    #         Reference Counting
    #
    #
    #     Ref(self, clone)
    #
    #         Makes this object refer to the data in clone.
    #         Parameters:	clone (wx.Object) – The object to ‘clone’.
    #
    #         Note
    #
    #         First this function calls UnRef on itself to decrement (and perhaps free) the data it is currently referring to. It then sets its own Object.m_refData to point to that of clone, and increments the reference count inside the data.
    #
    #         See also
    #
    #         UnRef , SetRefData , GetRefData , wx.ObjectRefData
    #
    #
    #     SetRefData(self, data)
    #
    #         Sets the Object.m_refData pointer.
    #         Parameters:	data (wx.ObjectRefData) –
    #
    #         See also
    #
    #         Ref , UnRef , GetRefData , wx.ObjectRefData
    #
    #
    #     UnRef(self)
    #
    #         Decrements the reference count in the associated data, and if it is zero, deletes the data.
    #
    #         The Object.m_refData member is set to None.
    #
    #         See also
    #
    #         Ref , SetRefData , GetRefData , wx.ObjectRefData
    #
    #
    #     UnShare(self)
    #
    #         This is the same of AllocExclusive but this method is public.
    #
    #
    #     Properties
    #
    #     ClassInfo
    #
    #         See GetClassInfo
    #
    #
    #     ClassName
    #
    #         See GetClassName
    #
    #
    #     RefData
    #
    #         See GetRefData and SetRefData
    ...

