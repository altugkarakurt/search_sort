#include "_c_search.h"

/*
    For 32-bit unsigned int 
*/
int linear_search32(uint32_t item, uint32_t *lst, size_t lst_len) {
    for(unsigned int i=0; i < lst_len; i++){
        if(lst[i] ==  item){
            return i;
        }
    }
    return -1;
}

int binary_search32(uint32_t item, uint32_t *lst, size_t lst_len) {
    int left_idx = 0;
    int right_idx = lst_len - 1;
    int mid_idx;

    while(left_idx <= right_idx){
        mid_idx = (left_idx + right_idx)/2;
        if(lst[mid_idx] < item)
            left_idx = mid_idx + 1;
        else if(lst[mid_idx] > item)
            right_idx = mid_idx - 1;
        else
            return mid_idx;
    }
    return -1;
}

int _bsearch_cmp32(const void* a, const void* b) {
    if(*(uint32_t*)a < *(uint32_t*)b)
        return -1;
    else if(*(uint32_t*)a > *(uint32_t*)b)
        return 1;
    else
        return 0;
}

int builtin_binary_search32(uint32_t item, uint32_t *lst, size_t lst_len) {
    uint32_t *p1 = (uint32_t*)bsearch(&item, lst, lst_len, sizeof(uint32_t), _bsearch_cmp32);

    if(p1 == NULL)
        return -1;
    return p1-lst;
}

/*
    For 8-bit unsigned int 
*/
int linear_search8(uint8_t item, uint8_t *lst, size_t lst_len) {
    for(unsigned int i=0; i < lst_len; i++){
        if(lst[i] ==  item){
            return i;
        }
    }
    return -1;
}

int binary_search8(uint8_t item, uint8_t *lst, size_t lst_len) {
    int left_idx = 0;
    int right_idx = lst_len - 1;
    int mid_idx;

    while(left_idx <= right_idx){
        mid_idx = (left_idx + right_idx)/2;
        if(lst[mid_idx] < item)
            left_idx = mid_idx + 1;
        else if(lst[mid_idx] > item)
            right_idx = mid_idx - 1;
        else
            return mid_idx;
    }
    return -1;
}

int _bsearch_cmp8(const void* a, const void* b) {
    return ( *(uint8_t*)a - *(uint8_t*)b );
}

int builtin_binary_search8(uint8_t item, uint8_t *lst, size_t lst_len) {
    uint8_t *p1 = (uint8_t*)bsearch(&item, lst, lst_len, sizeof(uint8_t), _bsearch_cmp8);

    if(p1 == NULL)
        return -1;
    return p1-lst;
}