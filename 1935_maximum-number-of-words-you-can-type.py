class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        can_type = dict()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            can_type[c] = c not in brokenLetters
        words = text.split()
        count = 0
        for word in words:
            if all(can_type[c] for c in word):
                count += 1
        return count
