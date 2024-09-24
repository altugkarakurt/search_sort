#include "_c_search.h"

/* To generate a .so file:

    gcc -c _c_search.c
    gcc _c_search.o -shared -o _c_search.so

*/

int linear_search(uint8_t item, uint8_t *lst, size_t lst_len) {
    for(unsigned int i=0; i < lst_len; i++){
        if(lst[i] ==  item){
            return i;
        }
    }
    return -1;
}

int binary_search(uint8_t item, uint8_t *lst, size_t lst_len) {
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