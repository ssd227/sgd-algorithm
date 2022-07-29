"""
另一本书上实现的方法还比我那个快一点，
而且还是没优化的，吐了。
from 《python algorithm》

todo 以后有时间再回头看看
"""

import random
import time


def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    # 1e5 cost time: 0.27900123596191406
    # 1e6 cost time: 3.4044387340545654

    t1 = time.time()

    li = [random.random() for _ in range(int(1e6))]
    mergesort(li)
    # print(quick_sort(li))

    print('cost time:', time.time() - t1)
