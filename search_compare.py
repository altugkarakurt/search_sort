from utils import time_search
from python_search_sort.py_search import py_binary_search, py_linear_search
from cy_search import cy_binary_search, cy_linear_search
from c_search_sort.c_search import c_binary_search, c_linear_search
import matplotlib.pyplot as plt


# Binary Search
lst_lens = [10**6, 25*10**5, 5*10**6, 75*10**5, 10**7, 25*10**6, 5*10**7, 75*10**6, 10**8]
time_elapsed = time_search([c_binary_search, cy_binary_search, py_binary_search], lst_lens)
for func_name in time_elapsed.keys():
    plt.loglog(lst_lens, [time_elapsed[func_name][ln] for ln in lst_lens], label=func_name)
plt.title("Run-time for Binary Search over Integer Arrays of Length n")
plt.xlabel("n")
plt.ylabel("Average Run-Time (s)")
plt.grid()
plt.xlim([lst_lens[0], lst_lens[-1]])
plt.legend()
plt.show()

# Linear Search
# lst_lens = [10**5, 25*10**4, 5*10**5, 75*10**4, 10**6, 25*10**5, 5*10**6, 75*10**5, 10**7]
# time_elapsed = time_search([c_linear_search, cy_linear_search, py_linear_search], lst_lens)
# for func_name in time_elapsed.keys():
#     plt.loglog(lst_lens, [time_elapsed[func_name][ln] for ln in lst_lens], label=func_name)
# plt.title("Run-time for Linear Search over Integer Arrays of Length n")
# plt.xlabel("n")
# plt.ylabel("Average Run-Time (s)")
# plt.grid()
# plt.xlim([lst_lens[0], lst_lens[-1]])
# plt.legend()
# plt.show()