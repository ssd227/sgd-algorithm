import collections
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    word = 'a' * 100000
    prefix = 'ab'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    print(param_2)
    param_3 = obj.startsWith(prefix)
    print(param_3)