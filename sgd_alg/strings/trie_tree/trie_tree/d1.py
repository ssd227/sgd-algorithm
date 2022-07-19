import collections

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

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        cur_node = self.root
        for c in prefix:

            if c not in cur_node.sub_path:
                return False
            else:
                cur_node = cur_node.sub_path.get(c)
        return True

if __name__ == '__main__':

    #Your Trie object will be instantiated and called as such:
    word = 'a'*200
    prefix = 'ab'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    print(param_2)
    param_3 = obj.startsWith(prefix)
    print(param_3)