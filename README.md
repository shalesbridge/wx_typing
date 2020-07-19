wx_typing
===============

This is a work in progress for typehints for the wxpython library.

## NOTES

There are a lot of filenames in this package that begin with an underscore.
These exist purely in an attempt to break up the large quantity of entries that
seem to be in wxpython's namespaces.

The leading underscore is to keep in line with the Python convention of using a
leading underscore to hint that something is "private"; end users (Python coders
using our stubs) should never need to import one of these themselves, nor even
know or care that they exist. Instead, they will get automatically pulled in by
the appropriate _\_\_init\_\_.py_
