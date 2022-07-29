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


if __name__ == '__main__':
    # 1e5 cost_time: 0.15999984741210938s
    # 1e6 cost_time: 2.509 -> 2.380 (插入排序带来的提升，好了一丢丢)
    li = [random.random() for _ in range(int(1e6))]
    quick_sort(li)
    # print(quick_sort(li))
