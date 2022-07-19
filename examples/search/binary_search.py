from sgd_alg.search.binary_search import binary_search


# 简单的有序数组作二分查找
def find_key_in_sort_list():
    li = [1, 3, 4, 4, 7]
    res1 = binary_search(li, key=7)
    print('key 7, find index is', res1)
    res2 = binary_search(li, key=5)
    print('key 5, not find result', res2)


if __name__ == '__main__':
    find_key_in_sort_list()
