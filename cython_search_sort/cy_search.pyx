#!python
#cython: language_level=3

import cython


def linear_search(item: cython.int, lst: cython.int[:]) -> cython.int:
    i: cython.int
    li: cython.int
    for i in range(lst.shape[0]):
        if(item == lst[i]):
            return i
    return -1

def binary_search(item: cython.int, lst: cython.int[:]) -> cython.int:
    left_idx: cython.int = 0
    right_idx: cython.int = len(lst)-1
    mid_idx: cython.int = 0
    while(left_idx <= right_idx):
        mid_idx = int((left_idx + right_idx)/2)
        if(lst[mid_idx] < item):
            left_idx = mid_idx + 1
        elif(lst[mid_idx] > item):
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1

"""
def binary_search(item: cython.object, lst: cython.object) -> cython.int:
    cy_item: cython.int = item
    cy_list: cython.int[:] = array.array('i', lst)
    left_idx: cython.int = 0
    right_idx: cython.int = len(cy_list)-1
    mid_idx: cython.int

    while(left_idx <= right_idx):
        mid_idx = int((left_idx + right_idx)/2)
        if(cy_list[mid_idx] < cy_item):
            left_idx = mid_idx + 1
        elif(cy_list[mid_idx] > cy_item):
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return None

cdef int linear_search(item: cython.object, lst: cython.object):
    cy_item: cython.int = item
    cy_list: cython.int[:] = array.array('i', lst)
    i: cython.int
    li: cython.int
    for i,li in enumerate(cy_list):
        if(cy_item == li):
            return i
    return -1
"""