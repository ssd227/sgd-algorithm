"""
思路：基于order array的二分查找方式，插入与删除操作需要整个移动 part of array items
这个复杂度代价过高，采用树型结构，利用链表的可操作性，降低复杂度

binary search tree的缺点：
    由于树的不平衡导致树的长度的无限制扩张，
    各种操作复杂度和树的高度密切相关，所以后续需要开发balance-tree算法

    树的结构和插入顺序有关、类似快排，随机化插入顺序理论上可以保证logN的复杂度
    最糟糕情况，退化为N

（也就是说，使用链表非常方便，但是多出了指针操作，
这个 系数 上多出的复杂度如果可以被 级数 复杂度上的降低所忽略，
就是采用多指针操作的好处，
todo 猜测：指针在内存上的不连续性，导致cpu上的cache miss 问题比数组型数据多）

跟着ppt基本实现了大框架
todo 验证算法的正确性和实用性
todo 删除操作时间复杂度为 根号N 还没搞明白
"""

from sgd_alg.search.symbol_table import STInterface


class Node:
    def __init__(self, k, v, lp=None, rp=None, count=0):
        self.key = k
        self.val = v
        self.left = lp
        self.right = rp
        self.count = count


class BSTree(STInterface):
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_(self.root, key, value)

    # todo 这种递归call容易超过最大深度啊，虽然写起来挺优美
    def put_(self, cur_node, key, value):
        if cur_node is None:
            return Node(key, value)
        if key < cur_node.key:
            cur_node.left = self.put_(cur_node.left, key, value)
        elif key > cur_node.key:
            cur_node.right = self.put_(cur_node.right, key, value)
        else:
            cur_node.val = value
        cur_node.count = 1 + self.size_(cur_node.left) + self.size_(cur_node.right)
        return cur_node

    def get(self, key):
        cur_node = self.root
        while cur_node:
            if key > cur_node.key:
                cur_node = cur_node.right
            elif key < cur_node.key:
                cur_node = cur_node.left
            else:
                return cur_node.val
        return None

    def min(self):
        return self.min_(self.root)

    def min_(self, cur_node=None):
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def max(self):
        return self.max_(self.root)

    def max_(self, cur_node=None):
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node

    def floor(self, key):
        return self.floor_(key, self.root).key

    # 注意：这里按容易理解的case顺序（可优化）
    def floor_(self, key, cur_node) -> Node:
        # case0 Null node
        if cur_node is None:
            return None
        # case1: k equals the key at root
        if key == cur_node.key:
            return cur_node
        # case2: k is less than the key at root
        elif key < cur_node.key:
            return self.floor_(key, cur_node.left)
        # case3: k is greater than the key at root
        else:
            # (if there is any key ≤ k in right subtree);
            # otherwise it is the key in the root.
            floor_node = self.floor_(key, cur_node.right)
            return floor_node if floor_node else cur_node

    def ceiling(self, key):
        pass

    def celling_(self, key):
        pass

    def rank(self, key):
        return self.rank_(key, self.root)

    def rank_(self, key, cur_node):
        if cur_node is None:
            return 0
        if key < cur_node.key:
            return self.rank_(key, cur_node.left)
        elif key > cur_node.key:
            return self.size_(cur_node.left) + 1 + self.rank_(key, cur_node.right)
        else:
            return self.size_(cur_node.left)

    def select(self):
        pass

    # 如果需要实现顺序遍历（树的中序遍历）
    # def iter(self):
    #     pass

    def delete_min(self):
        self.root = self.delete_min_(self.root)

    def delete_min_(self, cur_node):
        if cur_node.left is None:
            return cur_node.right
        cur_node.left = self.delete_min_(cur_node.left)
        cur_node.count = 1 + self.size_(cur_node.left) + self.size_(cur_node.right)
        return cur_node

    def delete(self, key):
        self.root = self.delete_(key, self.root)

    def delete_(self, key, cur_node):
        if cur_node is None:
            return None
        # search for key
        if key < cur_node.key:
            self.delete_(key, cur_node.left)
        elif key > cur_node.key:
            self.delete_(key, cur_node.right)
        else:  # equal

            # Case 0. [0 children] Delete t by setting parent link to null.
            # Case 1. [1 child] Delete t by replacing parent link.
            if cur_node.left is None:
                return cur_node.right
            if cur_node.right is None:
                return cur_node.left
            # Case 2. [2 children]
            right_left_min_node = self.min(cur_node.right)
            self.delete_min_(cur_node.right)
            cur_node.val = right_left_min_node.val

        cur_node.count = 1 + self.size_(cur_node.left) + self.size_(cur_node.right)
        return cur_node

    def contains(self, key) -> bool:
        raise NotImplementedError("Should have implemented this")

    def is_empty(self) -> bool:
        return self.root is None

    def size(self):
        return self.size_(self.root)

    def size_(self, node) -> int:
        if node is None:
            return 0
        return node.count
