#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

int linear_search32(uint32_t item, uint32_t *lst, size_t lst_len);
int binary_search32(uint32_t item, uint32_t *lst, size_t lst_len);
int _bsearch_cmp32(const void* a, const void* b);
int builtin_binary_search32(uint32_t item, uint32_t *lst, size_t lst_len);

int linear_search8(uint8_t item, uint8_t *lst, size_t lst_len);
int binary_search8(uint8_t item, uint8_t *lst, size_t lst_len);
int _bsearch_cmp8(const void* a, const void* b);
int builtin_binary_search8(uint8_t item, uint8_t *lst, size_t lst_len);