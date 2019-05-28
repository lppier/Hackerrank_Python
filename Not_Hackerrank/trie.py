
class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.counter = 1
        self.children = []
        self.word_complete = False


