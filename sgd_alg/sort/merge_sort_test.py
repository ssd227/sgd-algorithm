"""
归并排序-问题排查

这个速度就正确了，难道是原地操作交换过多导致的问题

提速tips3：减少aux 和 a之间的拷贝次数，相互循环使用
"""

import random
from sgd_alg.util import calc_time
from sgd_alg.sort.insertion_sort import insertion_sort


@calc_time
def merge_sort(a):
    return merge_sort_(a)


def merge_sort_(a):
    # 提速tips1：小数组用插入排序，能提速一丢丢
    if len(a) <= 7:
        insertion_sort(a)
        return a
    # if len(a) <= 1:
    #     return a

    mid = len(a)//2
    left_sort = merge_sort_(a[:mid])
    right_sort = merge_sort_(a[mid:])



    # merge two part
    a_sort = left_sort+right_sort
    i, j = 0, mid

    # 提速tips2: 提速效果比tips1更小
    if a_sort[mid-1] < a_sort[mid]:
        return a_sort

    aux = a_sort.copy()
    for k in range(len(a_sort)):
        if i > mid-1:
            a_sort[k] = aux[j]
            j += 1
        elif j > len(a_sort)-1:
            a_sort[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a_sort[k] = aux[i]
            i += 1
        else:
            a_sort[k] = aux[j]
            j += 1

    return a_sort


if __name__ == '__main__':
    # 1e5 cost_time: cost_time: 0.32199907302856445s

    li = [random.random() for _ in range(int(1e3))]
    li_sort = merge_sort(li)
    print(li_sort)
