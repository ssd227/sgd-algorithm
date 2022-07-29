"""
bottom up mergesort

这种处理边际指针的真是太容易错了。
如果回报（效率）无明显提升，还是首选递归写法

todo 这种直接在原始位置改值的做法还是太慢，不清楚python底层的哪一步代价巨大
"""

import random
from sgd_alg.util import calc_time
from sgd_alg.sort.insertion_sort import insertion_sort


@calc_time
def buttom_up_merge_sort(a):
    sz = 1
    N = len(a)

    while sz < N:
        lo = 0
        # print('sz', sz)
        while lo < N-sz:
            # print(lo, lo+sz, min(N-1, lo+2*sz-1))
            merge(a, lo, lo+sz, min(N-1, lo+2*sz-1))
            # print(a[lo:min(N-1, lo+2*sz-1)+1])
            # print(a)
            lo += 2*sz
        sz *= 2


def merge(a, lo, mid, hi):
    # 排序包含lo和hi两个边界
    aux = a.copy()
    i = lo
    j = mid

    for k in range(lo, hi + 1):
        # print('kij', k, i, j)
        if i > mid-1:
            # print('c1')
            a[k] = aux[j]
            j += 1
        elif j > hi:
            # print('c2')
            a[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            # print('c3')
            a[k] = aux[i]
            i += 1
        else:
            # print('c4')
            a[k] = aux[j]
            j += 1

if __name__ == '__main__':
    # 1e4 cost_time: 0.1630079746246338s
    # 1e5 cost_time: 25.602545738220215s
    li = [random.random() for _ in range(int(1e5))]
    buttom_up_merge_sort(li)
    # print(li)