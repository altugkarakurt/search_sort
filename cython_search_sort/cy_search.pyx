#!python
#cython: language_level=3

import cython


###############################
# For 32-bit Unsigned Integers
###############################
def cy_linear_search32(item: cython.uint, lst: cython.uint[:]) -> cython.uint:
    cdef unsigned int i
    for i in range(lst.shape[0]):
        if(item == lst[i]):
            return i
    return -1

def cy_binary_search32(item: cython.uint, lst: cython.uint[:]) -> cython.uint:
    cdef unsigned int left_idx = 0
    cdef unsigned int right_idx = len(lst)-1
    cdef unsigned int mid_idx = 0
    while(left_idx <= right_idx):
        mid_idx = int((left_idx + right_idx)/2)
        if(lst[mid_idx] < item):
            left_idx = mid_idx + 1
        elif(lst[mid_idx] > item):
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1

###############################
# For 8-bit Unsigned Integers
###############################
def cy_linear_search8(item: cython.uchar, lst: cython.uchar[:]) -> cython.uint:
    cdef unsigned int i
    for i in range(lst.shape[0]):
        if(item == lst[i]):
            return i
    return -1

def cy_binary_search8(item: cython.uchar, lst: cython.uchar[:]) -> cython.uint:
    cdef unsigned int left_idx = 0
    cdef unsigned int right_idx = len(lst)-1
    cdef unsigned int mid_idx = 0
    while(left_idx <= right_idx):
        mid_idx = int((left_idx + right_idx)/2)
        if(lst[mid_idx] < item):
            left_idx = mid_idx + 1
        elif(lst[mid_idx] > item):
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1