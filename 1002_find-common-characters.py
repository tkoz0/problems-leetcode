class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ret = []
        for c in 'abcdefghijklmnopqrstuvwxyz':
            ret += [c]*min(w.count(c) for w in words)
        return ret
