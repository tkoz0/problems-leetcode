class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wset = set(words)
        ret = []
        def isconcat(w):
            if w in wset:
                return True
            for i in range(1,len(w)):
                if w[:i] in wset and isconcat(w[i:]):
                    return True
            return False
        for word in wset:
            for i in range(1,len(word)):
                if word[:i] in wset and isconcat(word[i:]):
                    ret.append(word)
                    break
        return ret
