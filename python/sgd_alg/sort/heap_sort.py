import random
import time

from sgd_alg.data_struct.heap import PriorityHeap


"""
堆排序不是stable的，依次取出把末尾值提到上部再sink，可能打乱排序。

Bottom line. Heapsort is optimal for both time and space, but:
    􀉾Inner loop longer than quicksort’s.
    􀉾Makes poor use of cache memory.
    􀉾Not stable.

todo 
    优化1： Build heap using bottom-up method，不用一个一个树的插入，类似B+树的构造
    优化2：不用一个一个的取出重新赋值，直接用内部的 树array 来保存最后的排序结果。
"""

def heap_sort(a, reverse=False):
    pheap = PriorityHeap(capacity=len(a), reverse=reverse)
    for x in a:
        pheap.insert(x)
    return [pheap.pop_head() for _ in range(len(a))]
