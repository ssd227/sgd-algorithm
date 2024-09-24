"""
二分搜索树 binary search tree

思路：
    基于有序数组的二分查找，插入与删除操作需要移动 part of array items
    复杂度过高，采用树型结构，利用链表的可操作性，降低操作代价

缺点：
    树节点的不平衡导致树的高度无限扩张，
    操作复杂度和树的高度相关， 后续改进为balance-tree算法（2-3树、红黑树、B树）

    树的结构和插入顺序有关
        随机化插入顺序理论上可以保证O(logN)复杂度（类似快排）
        最糟糕情况退化为O(N)

使用链表非常方便，但多了指针操作（但整体复杂度然降低）
    系数上多出的复杂度可以被忽略
    todo 指针在内存上的不连续性导致cpu上的cache miss问题比数组型数据多
        小数据集合上那种算法更快，需要实际硬件的测试

todo 验证算法的正确性和实用性
"""

from sgd_alg.search.symbol_table import STInterface


class Node:
    def __init__(self, k, v, lp=None, rp=None, count=1):
        self.key = k
        self.val = v
        self.left = lp
        self.right = rp

        # In each node, we store the number of nodes in the subtree rooted at that
            # node; to implement size(), return the count at the root.
        # Remark. This facilitates efficient implementation of rank() and select().
        self.count = count # Subtree counts 记录本节点+左右两子节点node个数（即kv对的个数）


class BST(STInterface):
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_(self.root, key, value)

    # todo 递归call易超最大调用栈深度，虽然写起来优美
    def put_(self, cur_node, key, value):
        if cur_node is None:
            return Node(key, value) # new node
        
        if key < cur_node.key:
            cur_node.left = self.put_(cur_node.left, key, value)
        elif key > cur_node.key:
            cur_node.right = self.put_(cur_node.right, key, value)
        else:
            cur_node.val = value
        
        # update state
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

    def min_(self, cur_node):
        assert cur_node is not None
        
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node # 返回最左（非None）子节点

    def max(self):
        return self.max_(self.root)

    def max_(self, cur_node):
        assert cur_node is not None
        
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node  # 返回最右（非None）子节点

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
            return self.size_(cur_node.left) # todo 针对可重复key的二叉树可能不对，数值不稳定

    def select(self):
        pass

    def iter(self):
        yield from self.inorder_traversal(self.root) 
    
    def inorder_traversal(self, node):
        if node is not None:
            yield from self.inorder_traversal(node.left)  # 访问左子树
            yield (node.key, node.value)  # 访问当前节点
            yield from self.inorder_traversal(node.right)  # 访问右子树

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
            target_node = cur_node
            cur_node = self.min(target_node.right)
            cur_node.right = self.delete_min_(target_node.right)
            cur_node.left = target_node.left
            
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
