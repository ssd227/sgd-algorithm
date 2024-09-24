"""
union find 问题
    调用方式
        uf = UF()                   新建uf类
        uf.union(a,b)->None         将a、b连接
        uf.connected(a,b)-> bool    a、b是否连同

    实现类
        UFInterface     -接口类
        QuickFindUF     -find操作O（1），connected操作N
        QuickUnionUF    -union操作（logN）
        UF              -最优实现，直接使用
"""


class UFInterface:
    def __init__(self):
        pass

    def union(self, p, q):
        raise NotImplementedError("Should have implemented this")

    def connected(self, p, q):
        raise NotImplementedError("Should have implemented this")


class QuickFindUF(UFInterface):
    """
    quick find uf对每个union的操作的复杂度为O(N),
    如果合并操作太多，N^2的复杂的无法接受

    Quick-find defect.
        *Union too expensive (N array accesses).
        *Trees are flat, but too expensive to keep them flat.
    """

    def __init__(self, n):
        self.n = n
        self.id = list(range(n))  # id from 0..n-1， 初始化数组的复杂度O(N)

    def union(self, p, q):  # 复杂度O(N)
        pid = self.id[p]
        qid = self.id[q]
        # qid的component全部改为pid, 并入前者
        for i in range(self.n):
            if self.id[i] == qid:
                self.id[i] = pid

    def connected(self, p, q):  # 复杂度O(1)
        return self.id[p] == self.id[q]


class QuickUnionUF(UFInterface):
    """
    quick union uf

    用数组表示树结构，而且是一个多叉树结构
    id[i]是父节点的数组下标
    如果id[i] = i, 表明当前树的根节点

    union: 合并树结构，p的根并入q的根节点下。
    find: leaf to node遍历，验证是否同根节点。

    存在多少不同的根节点，就有多少个component
    todo 启发：合理的降低树的高度，可以保证find操作的高效性。



    Quick-union defect.
        *Trees can get tall.
        *Find too expensive (could be N array accesses).
    """

    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))  # id from 0..n-1

    def union(self, p, q):
        p_rt = self.get_root(p)
        q_rt = self.get_root(q)
        self.parent[q_rt] = p_rt

    def connected(self, p, q):
        p_rt = self.get_root(p)
        q_rt = self.get_root(q)
        return p_rt == q_rt

    def get_root(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i


# todo 写测试验证算法的正确性，rank是否可以用tree height代替也可以尝试
# 可使用版本，NlogN的复杂度
# 1s钟处理数据和java版本相比为1:20
class UF(UFInterface):
    """
    在quick union的基础上添加改进
    1、平衡树结构-小子树链接到大子树上
    2、路径压缩，每次寻根操作都多次路径压缩。
    """

    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))  # id from 0..n-1， 初始化数组的复杂度O(N)
        self.rank = [0] * n
        self.count_ = n

    def union(self, p, q):
        # 寻根操作，附加树压缩
        rp = self.find_root(p)
        rq = self.find_root(q)
        if rp == rq:  # 保证count的计算准确，java里能提速，python里完全不行。可能
            return
        if self.rank[rp] > self.rank[rq]:
            self.parent[rq] = rp  # p is larger as tree root
        elif self.rank[rp] < self.rank[rq]:
            self.parent[rp] = rq  # q is larger as tree root
        else:
            self.parent[rq] = rp
            self.rank[rp] += 1
        self.count_ -= 1

    def connected(self, p, q):
        p_rt = self.find_root(p)
        q_rt = self.find_root(q)
        return p_rt == q_rt

    def find_root(self, i):
        leaf_id = i
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]  # path compression by halving
            i = self.parent[i]
        self.parent[leaf_id] = i
        return i

    def count(self):
        return self.count_
