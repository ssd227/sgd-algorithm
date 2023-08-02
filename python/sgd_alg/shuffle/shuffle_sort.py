import random

"""
shuffle sort

给每个位置生成随机数，
给随机数排序从而打乱原始队列

打乱效率不是很高啊，不如knuth_shuffle.
不推荐调用
"""


def shuffle_sort(li) -> list:
    ids = [(i, random.random()) for i in range(len(li))]

    # 用快排排序 todo 可以优化最快的排序手段
    ids.sort(key=lambda x: x[1])

    random_li = [li[x[0]] for x in ids]

    return random_li

