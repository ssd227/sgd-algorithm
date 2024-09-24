"""
红黑树 Left-leaning red-black BSTs

思路：
    Left-leaning red-black BSTs: 1-1 correspondence with 2-3 trees
    
    基于BST树改红黑树还挺简单，底层思路还是2-3树
"""

from sgd_alg.search.symbol_table import STInterface


RED = True
BLACK = False


class Node:
    def __init__(self, k, v, lp=None, rp=None, color=BLACK, count=1):
        self.key = k
        self.val = v
        self.left = lp
        self.right = rp
        self.color = color

        # In each node, we store the number of nodes in the subtree rooted at that
            # node; to implement size(), return the count at the root.
        # Remark. This facilitates efficient implementation of rank() and select().
        self.count = count # Subtree counts 记录本节点+左右两子节点node个数（即kv对的个数）



class LLRBT(STInterface):
    def __init__(self):
        self.root = None
        
    def isRed(self, node):
        if node: return node.color
        return False
    
    # Left rotation. Orient a (temporarily) right-leaning red link to lean left.
    def rotateLeft(self, h:Node)-> Node:
        assert self.isRead(h.right)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x
    
    # Right rotation. Orient a left-leaning red link to (temporarily) lean right.
    def rotateRight(self, h:Node)-> Node:
        assert self.isRead(h.left)
        x=h.left
        h.left=x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x
    
    # Color flip. Recolor to split a (temporary) 4-node.
    def flipColors(self, h:Node):
        assert not self.isRed(h)
        assert self.isRed(h.left)
        assert self.isRed(h.right)
        h.color = RED
        h.left.color = BLACK
        h.right.color = BLACK
    
    
    def put(self, key, value):
        self.root = self.put_(self.root, key, value)

    def put_(self, h:Node, key, value) -> Node:
        # insert at bottom (and color it red)
        if h is None:
            return Node(key, value, color=RED) # new node
        
        if key < h.key:
            h.left = self.put_(h.left, key, value)
        elif key > h.key:
            h.right = self.put_(h.right, key, value)
        else:
            h.val = value
        
        # lean left
        if self.isRed(h.right) and not self.isRed(h.left):
            h =  self.rotateLeft(h)
        # balance 4-node
        if self.isRed(h.left) and self.isRed(h.left.left):
            h =  self.rotateRight(h)
        # split 4-node
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColors(h)
        
        # update state
        h.count = 1 + self.size_(h.left) + self.size_(h.right)
        return h

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
