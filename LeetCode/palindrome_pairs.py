class TrieNode(object):

    def __init__(self):

        self.end = -1
        self.children = collections.defaultdict(TrieNode)
        self.isP_below = []


class TrieTree(object):

    def __init__(self):

        self.root = TrieNode()

    def add(self, word, index):

        node = self.root

        for i, letter in enumerate(reversed(word)):

            if self.isPalindrome(word[:len(word)-i]):
                node.isP_below.append(index)
            node = node.children[letter]

        node.end = index

    def isPalindrome(self, word):

        if len(word) <= 1:
            return True
        else:
            return word[0] == word[-1] and self.isPalindrome(word[1:-1])

    def search(self, word, index, res):

        node = self.root

        for i, letter in enumerate(word):

            if node.end >= 0 and node.end != index and self.isPalindrome(word[i:]):
                res.append([index, node.end])

            if letter not in node.children:
                return res
            node = node.children[letter]

        for p in node.isP_below:
            if index != p:
                res.append([index, p])

        if node.end >= 0 and index != node.end:
            res.append([index, node.end])

        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        Tree = TrieTree()

        for i, v in enumerate(words):

            Tree.add(v, i)

        res = []

        for i, v in enumerate(words):

            res = Tree.search(v, i, res)

        return res
