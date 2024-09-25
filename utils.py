import numpy as np
from numpy.random import randint
from random import random
from timeit import default_timer as timer
from copy import deepcopy
import pdb


"""--------------------------------------------------------------------
    Constants
--------------------------------------------------------------------"""
_INT_MIN = 0
_INT_MAX = 2**32 - 2


"""--------------------------------------------------------------------
    General Util Functions
--------------------------------------------------------------------"""
# Returns a log-range from 10^exp_min to 10^exp_max, interleaved with
# steps in step_lst
def logrange(exp_min, exp_max, step_lst=[1, 5]):
    # 10^exp_min, 10^(exp_min+1), ..., 10^exp_max
    exps = 10**np.arange(exp_min, exp_max)
    return np.append(np.outer(exps, step_lst).flatten().astype(int), 10**exp_max).tolist()

# Print if verbose, NOP if not
def printv(print_str, verbose=False):
    if(verbose):
        print(print_str)

# Preprocesses function parameters that are allowed to be passed as
# single terms of iterables. Wraps single items into singleton lists
def listify(*args):
    if(len(args) == 1):
        return args[0] if(isinstance(args[0], list)) else [args[0]]
    return [listify(arg) for arg in args]

"""--------------------------------------------------------------------
    Utils for Sorting
--------------------------------------------------------------------"""
# Generates $lst_cnt many random lists of length $lst_len to sort
def generate_sort_data(lst_len, lst_cnt, bit_cnt=8):
    int_min, int_max = 0, (2**bit_cnt-2)
    int_type = np.uint8 if(bit_cnt == 8) else np.uint32
    return randint(int_min, int_max, size=(lst_cnt, lst_len), dtype=int_type)


# Tests a sorting function by comparing it against sorted(.) 
# over random lists
def test_sort(sort_funcs, bit_cnt=8, lst_len=10, lst_cnt=100):
    for func in listify(sort_funcs):
        for lst in generate_sort_data(lst_len, lst_cnt, bit_cnt=bit_cnt):
            test_lst, sorted_lst = func(lst), np.sort(lst)
            if(sorted_lst != test_lst):
                print(f"{func.__module__}.{func.__name__} failed the test: Expected {sorted_lst}, got {test_lst}.")
                break
        else:
            print(f"{func.__module__}.{func.__name__} passed the test")

# Times sorting function(s)
def time_sort(sort_funcs, lst_lens=[10**4], lst_cnt=5, bit_cnt=8, verbose=False):
    sort_funcs, lst_lens = listify(sort_funcs, lst_lens)
    
    time_elapsed = {func.__name__:{lst_len:0 for lst_len in lst_lens}
                    for func in sort_funcs}

    for len_i, lst_len in enumerate(lst_lens):
        printv(f"({len_i+1}/{len(lst_lens)})---------------------", verbose)

        for _ in range(lst_cnt):
            lst = generate_sort_data(lst_len, 1, bit_cnt=bit_cnt)[0]

            # Since we sort in-place, a deepcopy is passed to the sort function
            for func in listify(sort_funcs):
                _lst = deepcopy(lst)
                start_time = timer()
                func(_lst)
                end_time = timer()
                time_elapsed[func.__name__][lst_len] += (end_time-start_time)/lst_cnt

        for func in sort_funcs:
            printv(f"{func.__module__}.{func.__name__} searched a {lst_len}-long list in {time_elapsed[func.__name__][lst_len]:.02g} seconds.", verbose)
        
    return time_elapsed

"""--------------------------------------------------------------------
    Utils for Searching (Sorted Lists)
--------------------------------------------------------------------"""
# Generates $lst_cnt many lists of size $lst_len to search through. With
# $hit_prob probability, the item being searched is in the list. We set miss
# item as (int_max+1) since the value will not appear in the list
def generate_search_data(lst_len, lst_cnt, bit_cnt=8):
    lsts = np.sort(generate_sort_data(lst_len, lst_cnt, bit_cnt=bit_cnt))
    items = [lst[randint(0, (lst_len-1))] for lst in lsts]
    return items, lsts

def test_search(search_funcs, lst_len=50, lst_cnt=100, bit_cnt=8):
    for func in listify(search_funcs):
        items, lsts = generate_search_data(lst_len, lst_cnt, bit_cnt=bit_cnt)

        for item, lst in zip(items, lsts):
            item_idx = func(item, lst)
            if(item_idx < 0):
                if(item in lst):
                    print(f"{func.__module__}.{func.__name__} failed: Missed the item {item} in {lst}.")
            elif(lst[item_idx] != item):
                print(f"{func.__module__}.{func.__name__} failed: False positive at idx:{item_idx} for the item {item} in {lst}.")
        else:
            print(f"{func.__module__}.{func.__name__} passed the test")

def time_search(search_funcs, lst_lens=[10**6], lst_cnt=25, bit_cnt=8, verbose=True):
    search_funcs, lst_lens = listify(search_funcs, lst_lens)
    
    time_elapsed = {func.__name__:{lst_len:0 for lst_len in lst_lens}
                    for func in search_funcs}

    for len_i, lst_len in enumerate(lst_lens):
        printv(f"({len_i+1}/{len(lst_lens)})---------------------", verbose)
        
        for _ in range(lst_cnt):
            items, lsts = generate_search_data(lst_len, 1, bit_cnt=bit_cnt)
            item, lst = items[0], lsts[0]

            for func in search_funcs:
                _lst = deepcopy(lst)
                start_time = timer()
                func(item, _lst)
                end_time = timer()
                time_elapsed[func.__name__][lst_len] += (end_time-start_time)/lst_cnt

        for func in search_funcs:
            printv(f"{func.__module__}.{func.__name__} searched a {lst_len}-long list in {time_elapsed[func.__name__][lst_len]:.02g} seconds.", verbose)
    
    return time_elapsed
    