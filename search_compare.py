from utils import time_search
from python_search_sort.py_search import py_binary_search, py_linear_search
from cy_search import cy_binary_search, cy_linear_search
from c_search_sort.c_search import c_binary_search, c_linear_search

list_lens = [10**i for i in range(6,10)] # list of size 10^6,...,10^9

print("Comparing Binary Search Implementations:")
for lst_len in list_lens:
    time_search([c_binary_search, cy_binary_search, py_binary_search], lst_len=lst_len)
    print("--------------------------------------------------")

# print("Comparing Linear Search Implementations:")
# for lst_len in list_lens:
#     time_search([py_linear_search, cy_linear_search, c_linear_search], lst_len=lst_len)
#     print("--------------------------------------------------")