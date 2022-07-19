import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for c in word:
            cur_node = cur_node.children[c]
        cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def iter(s, cur_node):
            if len(s) == 0:
                if cur_node is not None:
                    return cur_node.is_word
                else:
                    return False

            c = s[0]
            if c != '.':
                cur_node = cur_node.children.get(c)
                return iter(s[1:], cur_node)
            else:
                flag = False
                for k in cur_node.children:
                    tmp_node = cur_node.children.get(k)
                    res = iter(s[1:], tmp_node)
                    if res:
                        flag = True
                        break
                return flag

        return iter(word, self.root)

#Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
a = 'abcde'
b = 'a.cde'

obj.addWord(a)
param_2 = obj.search(b)
print(param_2)