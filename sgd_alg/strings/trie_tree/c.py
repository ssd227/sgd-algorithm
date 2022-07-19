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


class Solution:

    def findWords(self, board, words):
        res = set()

        def dfs(mat, i, j, prefix):

            if not trie.startsWith(prefix):
                return
            if trie.search(prefix):
                res.add(prefix)
                #print('add', prefix)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ii = i + dx
                jj = j + dy

                if 0 <= ii < R and 0 <= jj < C and mat[ii][jj] != '':
                    w = mat[ii][jj]
                    mat[ii][jj] = ''
                    dfs(mat, ii, jj, prefix+w)
                    mat[ii][jj] = w

        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)

        R = len(board)
        C = len(board[0])

        for i in range(R):
            for j in range(C):
                w = board[i][j]
                board[i][j] = ''
                dfs(board, i, j, w)
                board[i][j] = w

        return list(res)

if __name__ == '__main__':
    b = [['a']]
    h = ["a"]

    res = Solution().findWords(b,h)
    print(res)