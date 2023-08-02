"""
快排

Preserving randomness. Shuffling is needed for performance guarantee
但是这里没有实现

"""
import random

from sgd_alg.sort.insertion_sort import insertion_sort
from sgd_alg.util import calc_time



@calc_time
def quick_sort(a):
    return quick_sort_(a)


def quick_sort_(a):
    if len(a) <= 7:
        insertion_sort(a)
        return a
    # if len(a) <= 1:
    #     return a

    povit = a[0]
    # 这么写由于遍历两边a[1:] 速度会慢1.5倍左右
    # left = [x for x in a[1:] if x <= povit]
    # right = [x for x in a[1:] if x > povit]
    left = []
    right = []
    for x in a[1:]:
        if x <= povit:
            left.append(x)
        else:
            right.append(x)

    sort_left = quick_sort_(left)
    sort_right = quick_sort_(right)

    return sort_left + [povit] + sort_right