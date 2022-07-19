import collections
import sys

class Node:
    def __init__(self):
        self.sub_path = collections.defaultdict(Node)  # k v
        self.count = 0

    def is_valid(self):
        return self.count > 0


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root

        for c in word:
            cur_node = cur_node.sub_path[c]
            cur_node.count += 1



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        cur_node = self.root
        for c in word:

            if c not in cur_node.sub_path:
                return False
            else:
                cur_node = cur_node.sub_path.get(c)

        return cur_node.is_valid()



    def find_identi_prefix(self,s):
        cur_node = self.root
        for i in range(len(s)):
            c = s[i]

            cur_node = cur_node.sub_path.get(c)
            if cur_node.count ==1:
                return i

        return len(s)-1


if __name__ == '__main__':
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    lines = []
    for _ in range(n):
        line = sys.stdin.readline().strip()
        lines.append(line)

    #print(lines)

    # insert all string
    tri = Trie()
    for line in lines:
        tri.insert(line)

    for l in lines:
        end_id = tri.find_identi_prefix(l)
        print(l[:end_id+1])
