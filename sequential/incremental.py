from math import log2


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

    # TODO iterate from the end not the beginning in the inner loop

"""--------------------------------------------------------------------
Generalizes insertion-sort by locally sorting sublists instead of
adjacent pairs. The sublists are taken by considering every n^th element
in the list with n called the gap.
We approximate the gaps in the original design that go as
len(lst)/2, len(lst)/4, len(lst)/8, ..., 1 or equivalently
2^t, 2^(t-1),..., 2^(t-t) for t = log2(len(lst)/2)
--------------------------------------------------------------------"""
def shell_sort(lst):
    t = round(log2(len(lst)))-1
    gaps = [2**(t-n) for n in range(t+1)]

    for gap in gaps:
        for i in range(gap):
            # lst[i::gap] = lst[i], lst[i+gap], lst[i+2*gap], ...
            lst[i::gap] = insertion_sort(lst[i::gap])
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
