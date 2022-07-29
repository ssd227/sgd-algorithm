import random

"""
思路类似于水塘抽样

由于随机数种子的选取有限，所以还是伪随机数
todo 证明一下概率
"""

def knuth_shuffle(li):
    for i in range(1, len(li)):
        idx = random.randint(0, i)
        if idx != i:
            li[idx], li[i] = li[i], li[idx]


if __name__ == '__main__':
    li = list(range(10))
    knuth_shuffle(li)
    print(li)
