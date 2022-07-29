"""
选择排序

for i 到 n：
    min_id = i
    for j 到 n：
        if vj < vi：
            更新min_id = j
    交换vi 和v_min_id (保证vi为剩下的数中最小的)

最好情况=最坏情况，时间复杂度：O(N^2)
数据移动较少，线性。外层循环交换一步到位

Running time insensitive to input.
Quadratic time, even if input is sorted.
Data movement is minimal. Linear number of exchanges.
"""


def selection_sort(li):
    for i in range(len(li)):
        min_id = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_id]:
                min_id = j
        if min_id != i:
            li[i], li[min_id] = li[min_id], li[i]


if __name__ == '__main__':
    a = [4, 76, 7, 8, 3, 72, 723, -325, 1]

    selection_sort(a)
    print(a)
