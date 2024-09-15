from random import randint
from timeit import default_timer as timer

from sequential.incremental import insertion_sort, shell_sort, bubble_sort
from sequential.decrease_conquer import selection_sort, heap_sort
from sequential.divide_conquer import quick_sort,merge_sort_bottom_up, merge_sort_top_down

# Generates $lst_cnt many random lists of length $lst_len to sort
def generate_data(lst_len, lst_cnt, int_min=0,int_max=100):
    return [[randint(int_min, int_max) for _ in range(lst_len) ]
             for _ in range(lst_cnt)]

# Tests a sorting function by comparing it against sorted(.) 
# over random lists
def test_sort(sort_func, lst_len=10, lst_cnt=100):
    if(callable(sort_func)):
        sort_func = [sort_func]
    
    for func in sort_func:
        lsts = generate_data(lst_len, lst_cnt)
        
        for lst in lsts:
            test_lst, sorted_lst = func(lst), sorted(lst)
            if(sorted_lst != test_lst):
                print(f"{func.__name__} failed the test: Expected {sorted_lst}, got {test_lst}.")
                break
        else:
            print(f"{func.__name__} passed the test")

# Times sorting function(s)
def time_sort(sort_func, lst_len=1000, lst_cnt=50):
    if(callable(sort_func)):
        sort_func = [sort_func]
    
    for func in sort_func:
        lsts = generate_data(lst_len, lst_cnt)
        start_time = timer()
        for lst in lsts:
            func(lst)
        end_time = timer()
        avg_time = (end_time-start_time)/lst_cnt

        print(f"{func.__name__} sorts a {lst_len}-long list in {avg_time:.02g} seconds.")
    