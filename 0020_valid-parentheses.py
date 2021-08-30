class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[': # open
                stack.append(c)
            else: # close, must have match on stack
                if not stack:
                    return False
                if {'(':')','{':'}','[':']'}[stack.pop()] != c:
                    return False
        return not stack # must have closed all
