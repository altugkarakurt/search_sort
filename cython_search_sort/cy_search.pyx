#!python
#cython: language_level=3

import cython


# cython.uchar = unsigned char = uint8_t in C.
def cy_linear_search(item: cython.uchar, lst: cython.uchar[:]) -> cython.int:
    i: cython.int
    for i in range(lst.shape[0]):
        if(item == lst[i]):
            return i
    return -1

def cy_binary_search(item: cython.uchar, lst: cython.uchar[:]) -> cython.int:
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
