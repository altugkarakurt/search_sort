from cython.cimports.cpython import array
import array

import cython


def linear_search(item: cython.object, lst: cython.object) -> cython.int:
    i: cython.int
    li: cython.int
    cy_item: cython.int = item
    cy_list: cython.int[:] = array.array('i', lst)
    for i,li in enumerate(cy_list):
        if(cy_item == li):
            return i
    return None
