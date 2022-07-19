class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        Root = None

        def fill_tree(p1, p2, pc):

            if p1 and p2:  # 都不为空
                pc = TreeNode(p1.val + p2.val)
                pc.left = fill_tree(p1.left, p2.left, pc.left)
                pc.right = fill_tree(p1.right, p2.right, pc.right)
                return pc

            if not p1 and not p2:  # 都为空
                return None

            # 一个为空
            if p1:
                pc = TreeNode(p1.val)
                pc.left = fill_tree(p1.left, None, pc.left)
                pc.right = fill_tree(p1.right, None, pc.right)
                return pc
            else:
                pc = TreeNode(p2.val)
                pc.left = fill_tree(None, p2.left, pc.left)
                pc.right = fill_tree(None, p2.right, pc.right)
                return pc

        Root = fill_tree(t1, t2, Root)
        return Root
