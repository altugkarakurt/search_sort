from utils import logrange, time_search
from python_search_sort.py_search import py_binary_search, py_linear_search

import matplotlib.pyplot as plt
import json

BIT_CNT = 32 # 8-bit or 32-bit integers

if(BIT_CNT == 32):
    from cy_search import cy_binary_search32 as cy_binary_search
    from cy_search import cy_linear_search32 as cy_linear_search
    from c_search_sort.c_search import c_binary_search32 as c_binary_search
    from c_search_sort.c_search import c_bsearch32 as c_bsearch
    from c_search_sort.c_search import c_linear_search32 as c_linear_search

else: # bit_cnt = 8
    from cy_search import cy_binary_search8 as cy_binary_search
    from cy_search import cy_linear_search8 as cy_linear_search
    from c_search_sort.c_search import c_binary_search8 as c_binary_search
    from c_search_sort.c_search import c_bsearch8 as c_bsearch
    from c_search_sort.c_search import c_linear_search8 as c_linear_search

"""--------------------------------------------------------------------
    Binary Search
--------------------------------------------------------------------"""
# Parameters
lst_lens = logrange(4,8)
binary_search_funcs = [c_bsearch, c_binary_search, cy_binary_search, py_binary_search]

# Timing the search
time_elapsed = time_search(binary_search_funcs, lst_lens, lst_cnt=100, bit_cnt=BIT_CNT)
with open(("./results/binary_search_%dbits.json" % (BIT_CNT)), "w") as f:
    json.dump(time_elapsed, f, indent=4)

# Visualization
plt.clf()
for func_name in time_elapsed.keys():
    plt.loglog(lst_lens, [time_elapsed[func_name][ln] for ln in lst_lens], label=func_name)
plt.title("Run-time for Binary Search over %d-bit Integers of Length n" % BIT_CNT)
plt.xlabel("n")
plt.ylabel("Average Run-Time (s)")
plt.grid()
plt.xlim([lst_lens[0], lst_lens[-1]])
plt.legend()
plt.savefig("./results/binary_search_%dbits.png" % (BIT_CNT))
# plt.show()

"""--------------------------------------------------------------------
    Linear Search
--------------------------------------------------------------------"""
# Parameters
lst_lens = logrange(4,7)
linear_search_funcs = [c_linear_search, cy_linear_search, py_linear_search]

# Timing the search
time_elapsed = time_search(linear_search_funcs, lst_lens, lst_cnt=100, bit_cnt=BIT_CNT)
with open(("./results/linear_search_%dbits.json" % (BIT_CNT)), "w") as f:
    json.dump(time_elapsed, f, indent=4)

# Visualization
plt.clf()
for func_name in time_elapsed.keys():
    plt.loglog(lst_lens, [time_elapsed[func_name][ln] for ln in lst_lens], label=func_name)
plt.title("Run-time for Linear Search over %d-bit Integers of Length n" % BIT_CNT)
plt.xlabel("n")
plt.ylabel("Average Run-Time (s)")
plt.grid()
plt.xlim([lst_lens[0], lst_lens[-1]])
plt.legend()
plt.savefig("./results/linear_search_%dbits.png" % BIT_CNT)
# plt.show()
