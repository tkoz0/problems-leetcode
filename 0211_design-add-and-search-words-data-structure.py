from typing import *
class Node:
    def __init__(self):
        self.children = dict()
        self.contained = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.contained = True

    def helper(self, word: str, root: Node) -> bool:
        if word == '':
            return root.contained
        if word[0] == '.':
            for letter in root.children:
                if self.helper(word[1:],root.children[letter]):
                    return True
            return False
            #return any(self.helper(word[1:],root.children[letter]) for letter in root.children)
        if word[0] in root.children:
            return self.helper(word[1:],root.children[word[0]])
        return False

    def search(self, word: str) -> bool:
        return self.helper(word,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
