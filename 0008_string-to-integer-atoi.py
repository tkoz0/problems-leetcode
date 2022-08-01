class Solution:
    def myAtoi(self, s: str) -> int:
        while len(s) > 0 and s[0] == ' ':
            s = s[1:]
        if len(s) == 0:
            return 0
        result = 0
        if s[0] == '-':
            neg = True
            s = s[1:]
        else:
            neg = False
            if s[0] == '+':
                s = s[1:]
        while len(s) > 0 and s[0].isdigit():
            result = 10*result + ord(s[0])-ord('0')
            s = s[1:]
        if neg:
            result = -result
        if result >= 2**31:
            result = 2**31-1
        if result < -2**31:
            result = -2**31
        return result
