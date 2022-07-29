"""
希尔排序

大h-sort，排序数量少。
小h-sort，基本上已经排好了。
基于之前的插入排序对这种情况有利，接近于ON的时间复杂度。

todo 怎么证明小h-sort不会打乱大h-sort的序。
todo 极限压力测试，但是时间复杂度不会降低到快排那么好。

老头认为的最优参数，怎么来的不太清楚
Sedgewick. 1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, …
Good. Tough to beat in empirical studies.
merging of (9 ⨉ 4^i) – (9 ⨉ 2^i) + 1
and 4^i – (3 ⨉ 2^i) + 1
"""

import random
from sgd_alg.util import calc_time


@calc_time
def shell_sort(li):
    # 确定最大h，然后逐步递减。这里使用h=3h+1
    h = 1
    while True:
        if (3 * h + 1) < len(li):
            h = 3 * h + 1
        else:
            break
    # 多轮 h-sort
    while h >= 1:
        # h-gap insert sort
        for i in range(h, len(li)):
            j = i
            while j >= h:
                if li[j] < li[j - h]:
                    li[j], li[j - h] = li[j - h], li[j]
                    j -= h
                else:
                    break
        h = h // 3


if __name__ == '__main__':
    # a = [4, 76, 7, 8, 3, 72, 723, -325, 1]

    # 1e4 cost_time: 0.04799771308898926
    # 1e5 cost_time: 0.7909963130950928
    # 1e6 cost_time: 13.919885873794556s
    # 还是比较慢的算法

    a = [random.random() for _ in range(int(1e6))]
    shell_sort(a)
    # print(a)
