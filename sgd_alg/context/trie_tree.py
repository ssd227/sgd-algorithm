# trie树常用于搜索提示。如当输入一个网址，可以自动搜索出可能的选择。
# 当没有完全匹配的搜索结果，可以返回前缀最相似的可能。

import collections

class TrieNode:
    def __init__(self):
        """
        节点内不存储任何val，只依赖defaultdict的key值来保存树的路径

        defaultdict operator：
            []:     if key not exist, create a node with this key
            get:    if key not exist， return None
        """
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node.children[letter]
        cur_node.is_word = True

    def search(self, word):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node.children.get(letter)
            if cur_node is None:
                return False
        return cur_node.is_word

    def startsWith(self, prefix):
        cur_node = self.root
        for letter in prefix:
            cur_node = cur_node.children.get(letter)
            if cur_node is None:
                return False
        return True
