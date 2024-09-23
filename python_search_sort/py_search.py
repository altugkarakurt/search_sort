"""--------------------------------------------------------------------
Simple linear search that traverses from beginning to end until it finds
the item. The only search algorithm implemented here that doesn't 
require $lst to be sorted. 
--------------------------------------------------------------------"""
def py_linear_search(item, lst):
    for i,li in enumerate(lst):
        if(item == li):
            return i
    return -1

"""--------------------------------------------------------------------
Assumes $lst is sorted, compares it to the mid-point and accordingly
picks the lower or higher half of the list. Recursively halves the list

_max_lt_idx flag is for internal use, where a failed search returns the
index of the largest entry less than $item instead of -1. The return
value -1 means it is smaller than all terms in the list.
--------------------------------------------------------------------"""
def py_binary_search(item,lst,_max_lt_idx=False):
    left_idx, right_idx = 0, len(lst)-1
    while(left_idx <= right_idx):
        mid_idx = int((left_idx + right_idx)/2)
        if(lst[mid_idx] < item):
            left_idx = mid_idx + 1
        elif(lst[mid_idx] > item):
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1 if(not _max_lt_idx) else right_idx

def ternary_search(item,lst):
    pass

def interpolation_search(item,lst):
    pass

def jump_search(item,lst):
    pass

def exponential_search(item,lst):
    pass