from sgd_alg.data_struct.union_find import QuickUnionUF, QuickFindUF, UF
from sgd_alg.util import calc_time
import random


def ex_slow_uf():
    N = 10
    qf_uf = QuickFindUF(N)
    qu_uf = QuickUnionUF(N)

    union_op = [(4, 3), (3, 8), (6, 5), (9, 4),
                (2, 1), (8, 9), (5, 0), (7, 2),
                (6, 1), (1, 0), (6, 7)]

    for p, q in union_op:
        qf_uf.union(p, q)
        qu_uf.union(p, q)


@calc_time
def ex_fast_uf(N):
    uf = UF(N)
    for i in range(N):
        # 随机生成union操作
        p = random.randint(0, N - 1)
        q = random.randint(0, N - 1)
        uf.union(p, q)
    print('count:', uf.count())


if __name__ == '__main__':
    # 极限3000s（约一个小时），可以处理到1e9量级的数据NlogN, 但是爆内存
    # java 1e8 14秒， 调大heap内存，1e9估计100多秒可以算完。

    for x in range(7):
        items_num = pow(10, x)
        print('N:1e{}'.format(x), end='\t')
        ex_fast_uf(items_num)
