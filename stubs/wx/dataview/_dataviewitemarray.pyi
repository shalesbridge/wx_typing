from typing import Any

import wx.dataview

class DataViewItemArray:
    # def __getitem__
    # def __iter__
    # def __len__
    # def append
    # def insert
    # def iterator_next
    # def iterator_swigregister
    # def swigregister
    #
    # The following was gathered by using pdb to run "dir()" on an instantiated DataViewItemArray.
    # ['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'index']
    def append(self, item: wx.dataview.DataViewItem) -> None: ...
    #
    # Having to guess that these methods work the same way as standard Python list objects...
    # This type signature for index() is adapted from the list object's in typeshed (https://github.com/python/typeshed/blob/master/stdlib/2/__builtin__.pyi)
    def index(self, item: wx.dataview.DataViewItem, start: int = ..., stop: int = ...) -> int: ...
    def __contains__(self, item: wx.dataview.DataViewItem) -> bool: ...
    def insert(self, i: int, x: wx.dataview.DataViewItem) -> None: ...
    def __len__(self) -> int: ...
    ...
