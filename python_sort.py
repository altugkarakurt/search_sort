"""--------------------------------------------------------------------
We iterate from second item to the end, keeping the first i+1 terms
sorted. In iteration i, we insert item i into its sorted location in
the head.
--------------------------------------------------------------------"""
def insertion_sort(lst):
    for i,li in enumerate(lst[1:]):
        for j,lj in enumerate(lst[:i+1]):
            if(li < lj):
                lst[:i+2] = lst[:j] + [li,lj] + lst[j+1:i+1]
                break
    return lst

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
Iterate over pairs of terms and order them and keep doing so until a
pass completes without any reordering
--------------------------------------------------------------------"""
def bubble_sort(lst):
    is_sorted = False
    while(not is_sorted):
        is_sorted = True
        for i,li in enumerate(lst[:-1]):
            if(li > lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
    return lst

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def shell_sort(lst):
    pass

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def merge_sort(lst):
    pass

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def heap_sort(lst):
    pass

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def quick_sort(lst):
    pass

"""--------------------------------------------------------------------
--------------------------------------------------------------------"""
def quick3_sort(lst):
    pass