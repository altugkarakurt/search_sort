#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

int linear_search(uint8_t item, uint8_t *lst, size_t lst_len);
int binary_search(uint8_t item, uint8_t *lst, size_t lst_len);
int _bsearch_cmp(const void* a, const void* b);
int builtin_binary_search(uint8_t item, uint8_t *lst, size_t lst_len);