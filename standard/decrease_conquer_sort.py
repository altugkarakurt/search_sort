"""--------------------------------------------------------------------
We find the minimum in lst[i:] and use the head for the sorted sublist 
--------------------------------------------------------------------"""
def selection_sort(lst):
    for i in range(len(lst)-1):
        min_item, min_idx = lst[i], i
        for j,lj in enumerate(lst[i:]):
            if(lj < min_item):
                min_item, min_idx = lj, (i+j)
        if(min_idx != i):
            li = lst[i]
            lst = lst[:i] + [min_item, li] + lst[i+1:min_idx] + lst[min_idx+1:]
    return lst

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def heap_sort(lst):
    pass