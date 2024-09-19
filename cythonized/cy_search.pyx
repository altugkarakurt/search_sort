from cython.cimports.cpython import array
import array

import cython


def linear_search(item: cython.object, lst: cython.object) -> cython.int:
    cy_item: cython.int = item
    cy_list: cython.int[:] = array.array('i', lst)
    i: cython.int
    li: cython.int
    for i,li in enumerate(cy_list):
        if(cy_item == li):
            return i
    return None

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
