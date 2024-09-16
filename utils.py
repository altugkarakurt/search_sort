from random import randint, random
from timeit import default_timer as timer


"""--------------------------------------------------------------------
    Utils for Sorting
--------------------------------------------------------------------"""
# Generates $lst_cnt many random lists of length $lst_len to sort
def generate_sort_data(lst_len, lst_cnt, int_min=0, int_max=100):
    return [[randint(int_min, int_max) for _ in range(lst_len) ]
             for _ in range(lst_cnt)]

# Tests a sorting function by comparing it against sorted(.) 
# over random lists
def test_sort(sort_func, lst_len=10, lst_cnt=100):
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
    Utils for Searching (Sorted Lists)
--------------------------------------------------------------------"""
# Generates $lst_cnt many lists of size $lst_len to search through. With
# $hit_prob probability, the item being searched is in the list.  
def generate_search_data(lst_len, lst_cnt, hit_prob=0.9, int_min=0, int_max=100):
    lsts = [sorted([randint(int_min, int_max) for _ in range(lst_len)])
             for _ in range(lst_cnt)]
    
    items = [lst[randint(0, (lst_len-1))] if(random() < hit_prob) else -1 for lst in lsts]

    return items, lsts

def test_search(search_func, lst_len=50, lst_cnt=100, hit_prob=0.5):
    if(callable(search_func)):
        search_func = [search_func]
    
    for func in search_func:
        items, lsts = generate_search_data(lst_len, lst_cnt, hit_prob=0.9)

        for item, lst in zip(items, lsts):
            item_idx = func(item, lst)
            if(item_idx is None):
                if(item in lst):
                    print(f"{func.__name__} failed: Missed the item {item} in {lst}.")
            elif(lst[item_idx] != item):
                print(f"{func.__name__} failed: False positive at idx:{item_idx} for the item {item} in {lst}.")
        else:
            print(f"{func.__name__} passed the test")


def time_search(search_func, lst_len=10**6, lst_cnt=25, hit_prob=0.9):
    if(callable(search_func)):
        search_func = [search_func]
    
    for func in search_func:
        items, lsts = generate_search_data(lst_len, lst_cnt, hit_prob=0.9)
        start_time = timer()
        for item, lst in zip(items, lsts):
            func(item, lst)
        end_time = timer()
        avg_time = (end_time-start_time)/lst_cnt

        print(f"{func.__name__} searched a {lst_len}-long list in {avg_time:.02g} seconds.")
