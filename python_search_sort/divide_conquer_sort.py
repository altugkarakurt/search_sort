"""--------------------------------------------------------------------
Merges two sorted lists into a sorted list
--------------------------------------------------------------------"""
def _merge(lst1, lst2):
    i,j = 0,0
    merged_lst = []

    # Both lists still have unprocessed tails
    while(i < len(lst1) and j < len(lst2)):
        if(lst1[i] < lst2[j]):
            merged_lst.append(lst1[i])
            i += 1
        else: # lst1[i] < lst2[j]
            merged_lst.append(lst2[j])
            j += 1

    # One of the lists is exhausted, the other has only the maximum
    # elements to be appended to the end
    if(i < len(lst1)):
        merged_lst.extend(lst1[i:])
    else: # j < len(lst2)
        merged_lst.extend(lst2[j:])
    return merged_lst

"""--------------------------------------------------------------------
The recursive (top-down) implementation of merge sort. Input list is
recursively split into two until we divide the list into singletons.
Then, the singleton sets are merged in a sorted way. 
--------------------------------------------------------------------"""
def merge_sort(lst):
    if(len(lst) <= 1):
        return lst
    mid_idx = int(len(lst)/2)
    left_lst = merge_sort([li for li in lst[:mid_idx]])
    right_lst = merge_sort([li for li in lst[mid_idx:]])

    return _merge(left_lst, right_lst)

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def quick_sort(lst):
    pass

