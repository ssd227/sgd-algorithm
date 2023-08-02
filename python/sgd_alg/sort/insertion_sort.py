"""
插入排序（冒泡排序）

时间复杂度：
    最好情况 O(N)
    最坏情况 O(N^2)

对于基本排好序的队列，逼近线性
交换次数过多，每次冒泡都是一次数据交换

Best case.
    If the array is in ascending order, insertion sort makes
    N - 1 compares and 0 exchanges.

Worst case.
    If the array is in descending order (and no duplicates),
    insertion sort makes ~ ½ N 2 compares and ~ ½ N 2 exchanges.

randomly case
    To sort a randomly-ordered array with distinct keys,
    insertion sort uses ~ ¼ N 2 compares and ~ ¼ N 2 exchanges on average

"""


def insertion_sort(li):
    for i in range(1, len(li)):
        j = i
        while j > 0:
            if li[j] < li[j - 1]:
                li[j], li[j - 1] = li[j - 1], li[j]
                j -= 1
            else:
                break
