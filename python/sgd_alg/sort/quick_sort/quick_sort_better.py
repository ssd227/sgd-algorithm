"""
快排改进
    10一下的list直接用插入排序
    median-of-3 选取中值作为 povit（todo 没搞懂这个midianof3 这个函数）
    于povit重复的key的问题，直接保留原地
    3-way partitioning

优化过怎么还变慢了呢？
    插入排序确实有用

quick sort工业产品上的优化
Basic algorithm = quicksort.
    􀉾Cutoff to insertion sort for small subarrays.
    􀉾Partitioning scheme: Bentley-McIlroy 3-way partitioning.
    􀉾Partitioning item.
        – small arrays: middle entry
        – medium arrays: median of 3
        – large arrays: Tukey's ninther [next slide]


todo 用c类的语言，实现inplace的操作，
    python的底层代价还是太高了，搞不清优化方向
"""
import random
from sgd_alg.util import calc_time
from sgd_alg.sort.insertion_sort import insertion_sort


@calc_time
def quick_sort_3way(a):
    return quick_sort_(a)


def quick_sort_(a):
    # if len(a) <= 1:
    #     return a
    if len(a) <= 7:
        insertion_sort(a)
        return a

    povit = a[0]
    # 这么写由于遍历两边a[1:] 速度会慢1.5倍左右
    # left = [x for x in a[1:] if x <= povit]
    # right = [x for x in a[1:] if x > povit]
    left = []
    right = []
    equals = [povit]
    for x in a[1:]:
        if x < povit:
            left.append(x)
        elif x > povit:
            right.append(x)
        else:
            equals.append(x)

    sort_left = quick_sort_(left)
    sort_right = quick_sort_(right)

    return sort_left + equals + sort_right

