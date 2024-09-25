import numpy as np
import ctypes


c_search = ctypes.cdll.LoadLibrary("./c_search_sort/_c_search.so")

def c_linear_search(item, lst):
    return c_search.linear_search(ctypes.c_ubyte(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)),
                                  ctypes.c_int(len(lst)))

def c_binary_search(item, lst):
    return c_search.binary_search(ctypes.c_ubyte(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)),
                                  ctypes.c_int(len(lst)))

def c_bsearch(item, lst):
    return c_search.builtin_binary_search(ctypes.c_ubyte(item),
                                    lst.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte)),
                                    ctypes.c_int(len(lst)))