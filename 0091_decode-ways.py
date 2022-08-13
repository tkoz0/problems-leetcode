class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [0]*(len(s)+1)
        ways[0] = 1
        ways[1] = 1 if s[0] != '0' else 0
        for i in range(2,len(s)+1):
            if s[i-1] != '0':
                ways[i] += ways[i-1]
            if s[i-2] != '0' and int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]
        return ways[-1]
