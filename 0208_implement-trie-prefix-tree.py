# Node contains
# bool isword = true if this is inserted in the trie
# map[char->node] = map single letter to child node
class Node:
    def __init__(self):
        self.isword = False
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = Node()
            ptr = ptr.children[c]
        ptr.isword = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.isword

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

