from random import randint, random
from timeit import default_timer as timer

from sequential.sorting import insertion_sort, shell_sort, bubble_sort
from decrease_conquer.sorting import selection_sort, heap_sort
from divide_conquer.sorting import quick_sort,merge_sort_bottom_up, merge_sort_top_down


"""--------------------------------------------------------------------
    Utils for Sorting
--------------------------------------------------------------------"""
# Generates $lst_cnt many random lists of length $lst_len to sort
def generate_sort_data(lst_len, lst_cnt, int_min=0, int_max=100):
    return [[randint(int_min, int_max) for _ in range(lst_len) ]
             for _ in range(lst_cnt)]

# Tests a sorting function by comparing it against sorted(.) 
# over random lists
def test_sort(sort_func, lst_len=1000, lst_cnt=25):
    if(callable(sort_func)):
        sort_func = [sort_func]
    
    for func in sort_func:
        lsts = generate_sort_data(lst_len, lst_cnt)
        
        for lst in lsts:
            test_lst, sorted_lst = func(lst), sorted(lst)
            if(sorted_lst != test_lst):
                print(f"{func.__name__} failed the test: Expected {sorted_lst}, got {test_lst}.")
                break
        else:
            print(f"{func.__name__} passed the test")

# Times sorting function(s)
def time_sort(sort_func, lst_len=1000, lst_cnt=25):
    if(callable(sort_func)):
        sort_func = [sort_func]
    
    for func in sort_func:
        lsts = generate_sort_data(lst_len, lst_cnt)
        start_time = timer()
        for lst in lsts:
            func(lst)
        end_time = timer()
        avg_time = (end_time-start_time)/lst_cnt

        print(f"{func.__name__} sorts a {lst_len}-long list in {avg_time:.02g} seconds.")

"""--------------------------------------------------------------------
    Utils for Searching
--------------------------------------------------------------------"""
# Generates $lst_cnt many lists of size $lst_len to search through. With
# $hit_prob probability, the item being searched is in the list.  
def generate_search_data(lst_len, lst_cnt, hit_prob=0.9, is_sorted=False,
                         int_min=0, int_max=100):
    lsts = [[randint(int_min, int_max) for _ in range(lst_len) ]
             for _ in range(lst_cnt)]
    
    if(is_sorted):
        lsts = [sorted(lst) for lst in lsts]
    
    items = [lst[randint(0, (lst_len-1))] if(random() < hit_prob) else -1 for lst in lsts]

    return items, lsts

def time_search(search_func, lst_len=1000, lst_cnt=25, hit_prob=0.9,
                is_sorted=False):
    if(callable(sort_func)):
        search_func, is_sorted = [search_func], [is_sorted]
    
    for func, sort_bool in zip(search_func, is_sorted):
        items, lsts = generate_sort_data(lst_len, lst_cnt, hit_prob=0.9, is_sorted=sort_bool)
        start_time = timer()
        for item, lst in zip(items, lsts):
            func(item, lst)
        end_time = timer()
        avg_time = (end_time-start_time)/lst_cnt

        print(f"{func.__name__} searched a {lst_len}-long list in {avg_time:.02g} seconds.")
