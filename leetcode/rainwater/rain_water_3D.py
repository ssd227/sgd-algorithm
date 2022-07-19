class Node:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right

class Prority_queue:
    def __int__(self):
        self.root = None

    def push(self, x):
        if not self.root:
            self.root = Node(x)
        else:

    def pop(self, x):
        pass

    def is_empty(self):
        return self.root is None

    def top(self):
        pass


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
