import numpy as np
import ctypes


c_search = ctypes.cdll.LoadLibrary("./c_search_sort/_c_search.so")

###############################
# For 32-bit Unsigned Integers
###############################
def c_linear_search32(item, lst):
    return c_search.linear_search32(ctypes.c_uint32(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32)),
                                  ctypes.c_size_t(len(lst)))

def c_binary_search32(item, lst):
    return c_search.binary_search32(ctypes.c_uint32(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32)),
                                  ctypes.c_size_t(len(lst)))

def c_bsearch32(item, lst):
    return c_search.builtin_binary_search32(ctypes.c_uint32(item),
                                    lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32)),
                                    ctypes.c_size_t(len(lst)))

###############################
# For 8-bit Unsigned Integers
###############################
def c_linear_search8(item, lst):
    return c_search.linear_search8(ctypes.c_uint8(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
                                  ctypes.c_size_t(len(lst)))

def c_binary_search8(item, lst):
    return c_search.binary_search8(ctypes.c_uint8(item),
                                  lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
                                  ctypes.c_size_t(len(lst)))

def c_bsearch8(item, lst):
    return c_search.builtin_binary_search8(ctypes.c_uint8(item),
                                    lst.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),
                                    ctypes.c_size_t(len(lst)))