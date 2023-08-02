"""
归并排序

stable sort


问题：
这个实现比预想的要慢，1e4-1e5的情况就不太对了，不像NlogN复杂度了。
比快排的简单实现要慢的多。
"""

import random
from sgd_alg.util import calc_time


@calc_time
def merge_sort(a):
    merge_sort_(a, 0, len(a) - 1)


def merge_sort_(a, lo, hi):
    if hi <= lo:
        return

    mid = lo + (hi - lo) // 2
    merge_sort_(a, lo, mid)
    merge_sort_(a, mid + 1, hi)

    i = lo
    j = mid + 1
    # merge two part
    aux = a[::]  # 浅拷贝，传入对象指针时需要重新考虑代码正确性
    # print(lo, hi)
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1



