from setuptools import setup
from Cython.Build import cythonize

# To compile:
#   python setup.py build_ext --inplace

dev_mode = True

setup(
    name='cy_search_sort',
    ext_modules = cythonize("cython_search_sort/cy_search.pyx", annotate=dev_mode),
)