from utils import test_search
from python_search_sort.py_search import py_binary_search, py_linear_search
from c_search_sort.c_search import c_binary_search32
from c_search_sort.c_search import c_bsearch32
from c_search_sort.c_search import c_linear_search32

from c_search_sort.c_search import c_binary_search8
from c_search_sort.c_search import c_bsearch8
from c_search_sort.c_search import c_linear_search8

print("-------------------------------------\n8-BIT\n-------------------------------------\n")
test_search([py_binary_search, py_linear_search,c_binary_search8,c_bsearch8,c_linear_search8], bit_cnt=8)

print("-------------------------------------\n32-BIT\n-------------------------------------\n")
test_search([py_binary_search, py_linear_search,c_binary_search32,c_bsearch32,c_linear_search32], bit_cnt=32)